import express, { Express, json } from "express";
import conexion from "./sequelize";
import usuarioRouter from "../routes/usuario.routes";
import imagenRouter from "../routes/imagen.routes";
import productoRouter from "../routes/producto.routes";
import { v2 } from "cloudinary";
import compraRouter from "../routes/compra.routes";
import cors from "cors";
export class Server {
  // private => no podra ser accedido desde fuera de la clase
  // readonly => no podra ser modificado su valor afuera del constructor
  private readonly app: Express;
  private readonly puerto: unknown;

  constructor() {
    this.app = express();
    this.puerto = process.env.PORT || 8000;
    this.app.use(cors());
    this.bodyParser();
    this.rutas();
    v2.config({
      cloud_name: process.env.CLOUDINARY_NAME,
      api_key: process.env.CLOUDINARY_API_KEY,
      api_secret: process.env.CLOUDINARY_API_SECRET,
    });
  }

  private bodyParser() {
    this.app.use(json());
  }

  private rutas() {
    this.app.use(usuarioRouter);
    this.app.use(imagenRouter);
    this.app.use(productoRouter);
    this.app.use(compraRouter);
  }

  public start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );
      // puede recibir los siguientes parametros
      // force => resetear toda la base de datos con los cambios actuales
      // alter => tratara de cambiar la informacion modificada en el orm. y si no la logra completar, emitira un error
      await conexion.sync();
      console.log("Base de datos conectada exitosamente");
    });
  }
}
