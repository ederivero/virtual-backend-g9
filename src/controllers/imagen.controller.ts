import { Request, Response } from "express";
import { v2 } from "cloudinary";
import fs from "fs";

export const subirImagen = async (req: Request, res: Response) => {
  try {
    if (!req.file) {
      return res.status(400).json({
        message: "Archivo no encontrado",
        content: null,
      });
    }

    const data = await v2.uploader.upload(req.file.path, { folder: "usuario" });

    await fs.promises.unlink(req.file.path);

    return res.status(201).json({
      message: "Imagen subida exitosamente",
      content: { id: data.public_id },
    });
  } catch (error) {
    return res.status(500).json({
      message: "Error al subir la imagen",
    });
  }
};
