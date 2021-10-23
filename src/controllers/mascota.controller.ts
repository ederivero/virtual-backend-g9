import { plainToClass } from "class-transformer";
import { Request, Response } from "express";
import { HttpError } from "http-errors";
import { actualizarMascotaDto } from "../dtos/request/actualizar-mascota.dto";
import { crearMascotaDto } from "../dtos/request/crear-mascota.dto";
import Cliente from "../models/cliente.model";

export const crearMascota = async (req: Request, res: Response) => {
  const dto = plainToClass(crearMascotaDto, req.body);
  try {
    await dto.isValid();

    const { clienteId, ...mascota } = dto;
    // primero buscar el cliente segun su id
    // si no existe indicar un message que no existe
    // message: 'Cliente no existe' status 200
    const clienteEncontrado = await Cliente.findById(clienteId);

    if (!clienteEncontrado) {
      return res.json({
        message: "Cliente no existe",
        content: null,
      });
    }

    console.log(clienteEncontrado);

    clienteEncontrado.clienteMascotas.push(mascota);

    const resultado = await clienteEncontrado.save();

    return res.status(201).json({
      message: "Mascota registrada exitosamente",
      content: resultado,
    });
  } catch (error) {
    if (error instanceof HttpError) {
      return res.status(error.status).json(error);
    }
  }
};

export const actualizarMascota = async (req: Request, res: Response) => {
  const dto = plainToClass(actualizarMascotaDto, req.body);
  const { mascotaId, clienteId } = req.params; // mascota-id
  try {
    await dto.isValid();
    // encontrar ese cliente
    const clienteEncontrado = await Cliente.findById(clienteId);

    if (!clienteEncontrado) {
      return res.json({
        message: "El cliente no existe",
      });
    }
    // iterar el array de mascotas para encontrar esa mascota
    const { clienteMascotas } = clienteEncontrado;

    for (const mascota of clienteMascotas) {
      console.log(mascota._id);

      if (mascota._id && mascota._id == mascotaId) {
        console.log("si hay la mascota");
        mascota.mascotaFechaNacimiento =
          dto.mascotaFechaNacimiento ?? mascota.mascotaFechaNacimiento;

        mascota.mascotaNombre = dto.mascotaNombre ?? mascota.mascotaNombre;

        mascota.mascotaRaza = dto.mascotaRaza ?? mascota.mascotaRaza;

        mascota.mascotaSexo = dto.mascotaSexo ?? mascota.mascotaSexo;

        await clienteEncontrado.save();

        return res.json({
          message: "Mascota actulizada exitosamente",
          content: mascota,
        });
      }
    }
    // actualizar esa mascota

    // si en algun momento (cliente no existe, mascota no existe) emitir una respuesta que indique que no encontro dicha entidad
    return res.json({
      message: "No se encontro la mascota a actualizar",
    });
  } catch (error) {
    if (error instanceof HttpError) {
      return res.status(error.status).json(error);
    }
  }
};
