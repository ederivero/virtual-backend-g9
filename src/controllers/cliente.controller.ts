import { plainToClass } from "class-transformer";
import { Request, Response } from "express";
import { HttpError } from "http-errors";
import { ClienteDto } from "../dtos/request/cliente.dto";
import { ListarClienteDto } from "../dtos/request/listar-clientes.dto";
import Cliente from "../models/cliente.model";

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
  const dto = plainToClass(ListarClienteDto, req.query);
  try {
    await dto.isValid();

    const clientes = await Cliente.find();

    return res.status(200).json({
      content: clientes,
      message: null,
    });
  } catch (error) {
    if (error instanceof HttpError) {
      return res.status(error.statusCode).json(error);
    }
  }
};
