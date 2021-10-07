import express from "express";
import morgan from "morgan";
export class Server {
  constructor() {
    this.app = express();
    this.puerto = 8000;
    this.rutas();
  }

  rutas() {
    // agregamos el middleware de morgan para haga tracking a todas las consultas al backend
    this.app.use(morgan("dev"));

    this.app.get("/", (req, res) => {
      // req => Request => la informacion que me enviar el cliente
      // res => Response => la informacion que le voy a devolver al cliente
      res.send("Bienvenido a mi API");
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
