import { Router } from "express";
import * as compraController from "../controllers/compra.controller";

const compraRouter = Router();

compraRouter.post("/compra", compraController.crearCompra);

export default compraRouter;
