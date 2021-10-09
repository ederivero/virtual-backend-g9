import { Sequelize } from "sequelize";

export const conexion = new Sequelize(
  "postgresql://postgres:root@localhost:5432/tareas",
  { logging: false } // logging => indica si que quiere mostrar o no las consultas a la bd
);
