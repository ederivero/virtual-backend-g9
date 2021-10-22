import { Router } from "express";
import { listarClientes, registro } from "../controllers/cliente.controller";

const clienteRouter = Router();

clienteRouter.route("/cliente").post(registro).get(listarClientes);

export default clienteRouter;
