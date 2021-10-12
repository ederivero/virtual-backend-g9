import express, { json } from "express";
import { tareasRouter } from "../routes/tareas.routes";
import { conexion } from "./sequelize";
import cors from "cors";

export class Server {
  constructor() {
    this.app = express();
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
    // indicara si el contenido de la izquierda es Verdadero (tiene un valor) entonces usara ese, sino, usara el contenido de la derecha
    // diferencia con el nullish coalescing operator => NCO valida que no sea ni NULL ni UNDEFINED y el logical OR valida que no sea undefined
    this.puerto = process.env.PORT || 8000;
    // http://expressjs.com/en/resources/middleware/cors.html#configuration-options

    this.app.use(
      cors({
        origin: "*", //['https://mipagina.com', 'http://cms.mipagina.com']
        methods: "PUT", // en el caso de los metodos SIEMPRE el GET sera permitido SIEMPRE
        allowedHeaders: ["Content-Type"], // indicar las cabeceras que queremos recibir en nuestro backend
      })
    );
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
    this.app.use(tareasRouter);
  }
  start() {
    this.app.listen(this.puerto, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.puerto}`
      );

      try {
        // sincronizara todos los modelos creados en el ORM con la bd
        await conexion.sync();
        console.log("Base de datos conectada exitosamente");
      } catch (error) {
        console.log(error);
      }
    });
  }
}
