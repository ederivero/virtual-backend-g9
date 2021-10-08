import { Sequelize } from "sequelize";

export const conexion = new Sequelize(
  "postgresql://postgres:root@localhost:5432/tareas"
);
