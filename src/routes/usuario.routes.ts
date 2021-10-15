import { Router } from "express";

import * as usuarioController from "../controllers/usuario.controller";
import { authValidator } from "../middlewares/validator";

const usuarioRouter = Router();

usuarioRouter.post("/registro", usuarioController.registroController);
usuarioRouter.post("/login", usuarioController.login);
usuarioRouter.get("/me", authValidator, usuarioController.perfil);

export default usuarioRouter;
