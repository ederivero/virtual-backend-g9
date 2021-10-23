import { plainToClass } from "class-transformer";
import { Request, Response } from "express";
import { HttpError } from "http-errors";
import { ActualizarClienteDto } from "../dtos/request/actualizar-cliente.dto";
import { ClienteDto } from "../dtos/request/cliente.dto";
import { ListarClienteDto } from "../dtos/request/listar-clientes.dto";
import Cliente from "../models/cliente.model";
import {
  paginationHelper,
  paginationSerializer,
} from "../utils/paginator.helper";

export const registro = async (req: Request, res: Response) => {
  const dto = plainToClass(ClienteDto, req.body);
  try {
    await dto.isValid();

    const nuevoCliente = await Cliente.create(req.body);

    return res.status(201).json({
      content: nuevoCliente,
      message: "Cliente creado exitosamente",
    });
  } catch (error) {
    console.log(error);
    if (error instanceof HttpError) {
      return res.status(error.statusCode).json(error);
    }

    return res.status(500).json({ message: "error" });
  }
};

export const listarClientes = async (req: Request, res: Response) => {
  const dto = plainToClass(ListarClienteDto, {
    page: req.query?.page ? +req.query.page : undefined,
    perPage: req.query?.perPage ? +req.query.perPage : undefined,
  });
  try {
    await dto.isValid();
    const { page, perPage } = dto;

    const paginationParams = paginationHelper({ page, perPage });

    const total = await Cliente.count();
    const clientes = await Cliente.find()
      .skip(paginationParams?.skip ?? 0)
      .limit(paginationParams?.limit ?? 0);

    const infoPagina = paginationSerializer(total, { page, perPage });

    return res.status(200).json({
      content: { infoPagina, data: clientes },
      message: null,
    });
  } catch (error) {
    if (error instanceof HttpError) {
      return res.status(error.statusCode).json(error);
    }
  }
};

export const actualizarCliente = async (req: Request, res: Response) => {
  const { id } = req.params;

  const dto = plainToClass(ActualizarClienteDto, req.body);
  try {
    await dto.isValid();
    const clienteActualizado = await Cliente.findOneAndUpdate(
      { _id: id },
      { $set: dto },
      { new: true }
    );

    return res.status(200).json({
      content: clienteActualizado,
      message: null,
    });
  } catch (error) {
    if (error instanceof HttpError) {
      return res.status(error.statusCode).json(error);
    }
  }
};

export const eliminarCliente = async (req: Request, res: Response) => {
  const { id } = req.params;
  try {
    const clienteEliminado = await Cliente.findByIdAndDelete(id);
    // mediante el uso de un operador ternario indicar que si no hubo eliminacion, mostrar un status 404 y en el mssage 'No se encontro el cliente'
    return res.status(clienteEliminado ? 200 : 404).json({
      content: clienteEliminado,
      message: clienteEliminado
        ? "Cliente eliminado exitosamente"
        : "No se encontro el cliente",
    });
  } catch (error) {
    return res.status(500).json({
      content: null,
      message: "Error al eliminar el cliente",
    });
  }
};
