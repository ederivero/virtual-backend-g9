import { plainToClass } from "class-transformer";
import { Request, Response } from "express";
import { HttpError } from "http-errors";
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

export const actualizarProducto = (req: Request, res: Response) => {};
