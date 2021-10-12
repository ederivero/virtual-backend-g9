import { Router } from "express";

import * as tareasController from "../controllers/tareas.controller";
// import { crearTarea } from "../controllers/tareas.controller";

export const tareasRouter = Router();

tareasRouter
  .route("/tareas")
  .post(tareasController.serializadorTarea, tareasController.crearTarea)
  .get(tareasController.listarTareas);

tareasRouter
  .route("/tarea/:id")
  .put(tareasController.actualizarTarea)
  .delete(tareasController.eliminarTarea)
  .get(tareasController.devolverTarea);

tareasRouter.get("/buscarTarea", tareasController.filtrarTareas);
