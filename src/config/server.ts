import express, { Express, json } from "express";
import { connect } from "mongoose";

export default class Server {
  private readonly app: Express;
  private readonly port: string;

  constructor() {
    this.app = express();
    this.port = process.env.PORT ?? "8000";
    this.bodyParser();
  }
  private bodyParser() {
    this.app.use(json());
  }
  start() {
    this.app.listen(this.port, async () => {
      console.log(
        `Servidor corriendo exitosamente en el puerto ${this.port} 🚀🚀🚀`
      );
      try {
        await connect(process.env.DATABASE_URL ?? "");
        console.log("Servidor de base de datos conectado exitosamente");
      } catch (error) {
        console.log("Error al conectar la bd");
      }
    });
  }
}
