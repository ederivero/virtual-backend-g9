import { Request, Response } from "express";
import { Usuarios } from "../config/models";

export const registroController = async (req: Request, res: Response) => {
  try {
    const { body } = req;
    const nuevoUsuario = await Usuarios.create(body);

    // Metodo alternativo
    // primero se construye el objeto
    // const nuevoUsuario2 = Usuarios.build({usuarioNombre: 'Eduardo'})
    // nuevoUsuario2.setDataValue('usuarioNombre','asdads')
    // se guarda en la bd
    // await nuevoUsuario2.save()

    return res.status(201).json({
      content: nuevoUsuario,
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error,
    });
  }
};
