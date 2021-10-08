import { Router } from "express";
import {
  crearActividad,
  listarActividades,
  devolverActividad,
  actualizarActividad,
  eliminarActividad,
} from "../controllers/actividades";

export const actividades_router = Router();
actividades_router.post("/actividad", crearActividad);
actividades_router.get("/actividades", listarActividades);
// actividades_router.get("/actividad/:id", devolverActividad);
// actividades_router.put("/actividad/:id", actualizarActividad);
actividades_router
  .route("/actividad/:id")
  .get(devolverActividad)
  .put(actualizarActividad)
  .delete(eliminarActividad);
