import { Sequelize } from "sequelize";
require("dotenv").config();

export default new Sequelize(String(process.env.DATABASE_URL), {
  logging: false,
});
