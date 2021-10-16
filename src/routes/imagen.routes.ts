import { Router } from "express";
import { subirImagen } from "../controllers/imagen.controller";
import Multer from "multer";
import path from "path";

const multer = Multer({
  storage: Multer.diskStorage({
    destination: path.join(__dirname, "../../imagenes"),
    filename: (req, file, cb) => {
      cb(null, file.originalname);
    },
  }),
});

const imagenRouter = Router();

imagenRouter.post("/upload-image", multer.single("imagen"), subirImagen);

export default imagenRouter;
