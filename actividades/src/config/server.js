import express from "express";

export class Server {
  constructor() {
    this.app = express();
    this.puerto = 8000;
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
