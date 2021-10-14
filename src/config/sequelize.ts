import { Sequelize } from "sequelize";
require("dotenv").config();

export default new Sequelize(process.env.DATABASE_URL ?? "", {
  logging: false,
});
