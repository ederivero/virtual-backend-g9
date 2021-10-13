import express, { Express, json } from "express";
import conexion from "./sequelize";

export class Server {
  // private => no podra ser accedido desde fuera de la clase
  // readonly => no podra ser modificado su valor afuera del constructor
  private readonly app: Express;
  private readonly puerto: number;

  constructor() {
    this.app = express();
    this.puerto = 8000;
    this.bodyParser();
  }

  private bodyParser() {
    this.app.use(json());
  }

  public start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );
      await conexion.sync();
      console.log("Base de datos conectada exitosamente");
    });
  }
}
