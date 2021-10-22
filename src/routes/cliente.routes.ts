import { Router } from "express";
import { registro } from "../controllers/cliente.controller";

const clienteRouter = Router();

clienteRouter.route("/cliente").post(registro);

export default clienteRouter;
