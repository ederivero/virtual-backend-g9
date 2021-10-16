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

    const mensaje_error = errores.map((error) => error.constraints);

    return res.status(400).json({
      content: mensaje_error,
      message: "Campos invalidos",
    });
  }

  const trasaccion = await conexion.transaction();
  try {
    const nuevaCompra = await Compras.create(
      {
        compraFecha: new Date(),
        compraTotal: 0.0,
        usuarioId: req.usuario?.getDataValue("usuarioId"),
      },
      { transaction: trasaccion }
    );

    validador.detalle.map(async (detalle_compra) => {
      const producto = await Productos.findByPk(detalle_compra.producto, {
        attributes: ["productoCantidad", "productoPrecio"],
      });
      if (!producto) {
        throw new Error(`Producto ${detalle_compra.producto} no existe`);
      }
      // ahora validamos si hay la cantidad suficiente
      if (detalle_compra.cantidad > producto.getDataValue("productoCantidad")) {
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
    });
  } catch (error: unknown) {
    await trasaccion.rollback();
    return res.status(500).json({
      message: "Error al crear la compra",
      content: error instanceof Error ? error.message : "",
    });
  }

  return res.json({
    message: "Compra creada exitosamente",
  });
};
