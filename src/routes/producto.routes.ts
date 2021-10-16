import { Router } from "express";
import * as productoController from "../controllers/producto.controller";
import { adminValidator, authValidator } from "../middlewares/validator";
const productoRouter = Router();

productoRouter
  .route("/producto")
  .post(authValidator, adminValidator, productoController.crearProducto)
  .get(productoController.listarProducto);

export default productoRouter;
