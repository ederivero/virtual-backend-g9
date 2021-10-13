import { Sequelize } from "sequelize";
require("dotenv").config();

export const conexion = new Sequelize(
  process.env.DATABASE_URL2,
  { logging: false } // logging => indica si que quiere mostrar o no las consultas a la bd
);
