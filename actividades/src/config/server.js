import express, { json, urlencoded, raw } from "express";
import morgan from "morgan";
import { actividades_router } from "../routes/actividades";

export class Server {
  constructor() {
    this.app = express();
    this.puerto = 8000;
    this.cors();
    this.bodyParser();
    this.rutas();
  }

  bodyParser() {
    // sirve para indicar en el proyecto que formatos (bodys) me puede enviar el front (client)
    this.app.use(json());
    this.app.use(raw());
  }

  rutas() {
    // agregamos el middleware de morgan para haga tracking a todas las consultas al backend
    this.app.use(morgan("dev"));
    this.app.use(actividades_router);

    this.app.get("/", (req, res) => {
      // req => Request => la informacion que me enviar el cliente
      // res => Response => la informacion que le voy a devolver al cliente
      res.status(200).send("Bienvenido a mi API");
    });
  }

  cors() {
    this.app.use((req, res, next) => {
      // Access-Control-Allow-Origin => indica que origenes pueden acceder a mi api (si queremos todos ponemos el *)
      res.header("Access-Control-Allow-Origin", "*");

      // Access-Control-Allow-Headers => indica las cabeceras permitidas que puede enviar el cliente
      res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");

      // Access-Control-Allow-Methods => indica los metodos a los que puede acceder mi cliente
      res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");

      next();
    });
  }

  start() {
    this.app.listen(this.puerto, () => {
      // alt+96 ``
      console.log(`Servidor corriendo en el puerto ${this.puerto}`);
    });
  }
}

// export const x = 10;
// const x = 10;

// module.exports = {
//   x: x,
// };
