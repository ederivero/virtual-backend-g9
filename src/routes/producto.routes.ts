import { Router } from "express";
import * as productoController from "../controllers/producto.controller";

const productoRouter = Router();

productoRouter
  .route("/producto")
  .post(productoController.crearProducto)
  .get(productoController.listarProducto);

export default productoRouter;
