import { Request, Response, NextFunction } from "express";
import { verify } from "jsonwebtoken";
import { Model } from "sequelize";
import { Usuarios } from "../config/models";

export interface RequestUser extends Request {
  usuario?: Model;
}

export const authValidator = async (
  req: RequestUser,
  res: Response,
  next: NextFunction
) => {
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Se necesita una token para esta peticion",
      content: null,
    });
  }

  // Authorization : Bearer 123123123.123123123.123123123
  const token = req.headers.authorization.split(" ")[1];
  try {
    const payload = verify(token, process.env.JWT_TOKEN ?? "");

    if (typeof payload === "object") {
      const usuario = await Usuarios.findByPk(payload.usuarioId, {
        attributes: { exclude: ["usuarioPassword"] },
      });

      if (!usuario) {
        return res.status(400).json({
          message: "Usuario no existe en la bd",
        });
      }
      req.usuario = usuario;
    }

    next();
  } catch (error: unknown) {
    if (error instanceof Error) {
      return res.status(401).json({
        message: error.message,
        content: null,
      });
    }
  }
};
