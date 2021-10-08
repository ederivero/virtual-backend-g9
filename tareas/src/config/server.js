import express, { json } from "express";
import { conexion } from "./sequelize";

export class Server {
  constructor() {
    this.app = express();
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
    // indicara si el contenido de la izquierda es Verdadero (tiene un valor) entonces usara ese, sino, usara el contenido de la derecha
    // diferencia con el nullish coalescing operator => NCO valida que no sea ni NULL ni UNDEFINED y el logical OR valida que no sea undefined
    this.puerto = process.env.PORT || 8000;
    this.bodyParser();
    this.rutas();
  }
  bodyParser() {
    this.app.use(json());
  }
  rutas() {
    this.app.get("/", (req, res) => {
      res.json({
        message: "Bienvenido a mi API",
      });
    });
  }
  start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );

      try {
        await conexion.sync();
        console.log("Base de datos conectada exitosamente");
      } catch (error) {
        console.log(error);
      }
    });
  }
}
