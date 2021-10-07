import { Router } from "express";
import { crearActividad, listarActividades } from "../controllers/actividades";

export const actividades_router = Router();
actividades_router.post("/actividad", crearActividad);
actividades_router.get("/actividades", listarActividades);
