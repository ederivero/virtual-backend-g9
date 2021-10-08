import { Router } from "express";

import * as tareasController from "../controllers/tareas.controller";
// import { crearTarea } from "../controllers/tareas.controller";

export const tareasRouter = Router();

tareasRouter.route("/tareas").post(tareasController.crearTarea);
