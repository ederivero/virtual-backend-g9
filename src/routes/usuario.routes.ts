import { Router } from "express";

import * as usuarioController from "../controllers/usuario.controller";

const usuarioRouter = Router();

usuarioRouter.post("/registro", usuarioController.registroController);
usuarioRouter.post("/login", usuarioController.login);

export default usuarioRouter;
