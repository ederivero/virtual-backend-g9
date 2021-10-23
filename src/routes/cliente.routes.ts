import { Router } from "express";
import {
  actualizarCliente,
  eliminarCliente,
  listarClientes,
  registro,
} from "../controllers/cliente.controller";

const clienteRouter = Router();

clienteRouter.route("/cliente").post(registro).get(listarClientes);
clienteRouter
  .route("/cliente/:id")
  .put(actualizarCliente)
  .delete(eliminarCliente);

export default clienteRouter;
