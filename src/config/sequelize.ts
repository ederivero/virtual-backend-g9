import { Sequelize } from "sequelize";
require("dotenv").config();

export default new Sequelize(process.env.DATABASE_URL ?? "", {
  dialectOptions:
    process.env.NODE_ENV !== "production"
      ? {}
      : { ssl: { rejectUnauthorized: false } },

  logging: false,
});
