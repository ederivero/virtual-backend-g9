import { Router } from "express";
import {
  actualizarMascota,
  crearMascota,
} from "../controllers/mascota.controller";

const mascotaRouter = Router();

mascotaRouter.route("/mascota").post(crearMascota);
mascotaRouter
  .route("/cliente/:clienteId/mascota/:mascotaId")
  .put(actualizarMascota);
export default mascotaRouter;
