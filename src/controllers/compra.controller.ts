import { plainToClass } from "class-transformer";
import { validate } from "class-validator";
import { Request, Response } from "express";
import { Compras, Detalles, Productos } from "../config/models";
import { CompraDto, DetalleCompraDto } from "../dtos/request/compra.dto";
import conexion from "../config/sequelize";
import { RequestUser } from "../middlewares/validator";

export const crearCompra = async (req: RequestUser, res: Response) => {
  const validador = plainToClass(CompraDto, req.body);
  const errores = await validate(validador);

  if (errores.length !== 0) {
    // TODO: indicar los errores correctamente cuando se produzcan a raiz de un sub-error
    // if (errores[0].children) {
    //   console.log(errores[0].children[0].children);
    // }

    // ingreso a las constraints en primer nivel
    const mensaje_error = errores.map((error) => error.children);
    // ingresar en un segundo nivel y mapear esos errores nuevamente (ya que tenemos un DTO dentro de otro)
    const mensaje_error_final = mensaje_error.map((error) =>
      error?.map((error_hijo) => {
        console.log(error_hijo);
        // ingresaba a los errores del dto adyacente e ingresaba nuevamente a sus errores para ahora si devolver el constraint

        return error_hijo.children
          ? error_hijo.children.map(
              (error_hijo_hijo) => error_hijo_hijo.constraints
            )
          : null;
      })
    );
    console.log(mensaje_error);

    return res.status(400).json({
      content: mensaje_error_final,
      message: "Campos invalidos",
    });
  }

  const trasaccion = await conexion.transaction();
  try {
    // 1. Creo la compra (cabecera de la compra)
    const nuevaCompra = await Compras.create(
      {
        compraFecha: new Date(),
        compraTotal: 0.0,
        usuarioId: req.usuario?.getDataValue("usuarioId"),
      },
      { transaction: trasaccion }
    );

    // asi seria el uso sin la necesitad de un Promise.all y con un forin sencillo
    for (const key in validador.detalle) {
    }
    // asi seria el uso con la espera de un Promise.all (espera la ejecuion de todas las promesas)
    await Promise.all(
      validador.detalle.map(async (detalle_compra) => {
        const producto = await Productos.findByPk(detalle_compra.producto, {
          attributes: ["productoCantidad", "productoPrecio"],
        });
        if (!producto) {
          throw new Error(`Producto ${detalle_compra.producto} no existe`);
        }
        // ahora validamos si hay la cantidad suficiente
        if (
          detalle_compra.cantidad > producto.getDataValue("productoCantidad")
        ) {
          throw new Error(
            `Producto ${detalle_compra.producto} no hay suficiente cantidades`
          );
        }
        // ahora creamos el detalle de ese item
        await Detalles.create(
          {
            productoId: detalle_compra.producto,
            compraId: nuevaCompra.getDataValue("compraId"),
            detalleCantidad: detalle_compra.cantidad,
            detalleTotal:
              detalle_compra.cantidad * producto.getDataValue("productoPrecio"),
          },
          { transaction: trasaccion }
        );

        // disminuir la cantidad del item
        // UPDATE productos SET cantidad = cantidad - 1 WHERE id = '.....';
        await Productos.update(
          {
            productoCantidad:
              producto.getDataValue("productoCantidad") -
              detalle_compra.cantidad,
          },
          {
            where: {
              productoId: detalle_compra.producto,
            },
            transaction: trasaccion,
          }
        );
        const compra = await Compras.findByPk(nuevaCompra.getDataValue("id"));

        // await Compras.update({compraTotal: compra?.getDataValue('compraTotal')})
      })
    );
    await trasaccion.commit();
    return res.status(201).json({
      message: "Compra realizada exitosamente",
      content: nuevaCompra,
    });
  } catch (error: unknown) {
    await trasaccion.rollback();
    return res.status(500).json({
      message: "Error al crear la compra",
      content: error instanceof Error ? error.message : "",
    });
  }
};
