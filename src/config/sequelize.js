import { Sequelize } from "sequelize";
require("dotenv").config();

export const conexion = new Sequelize(
  process.env.DATABASE_URL,
  {
    logging: false,
    // para poder usar bd remotas de postgres que requiran configuracion especial
    dialectOptions:
      process.env.NODE_ENV === "production" // variable que define heroku en sus servidores indicando el contenido de production
        ? {
            // sirve para indicar que la bd no sea necesario que tenga certificado SSL y si es que no lo tiene con el rejectUnauthorized = false  indicaremos que no emita el error y que normal se conecte.
            ssl: {
              rejectUnauthorized: false,
            },
          }
        : {},
  } // logging => indica si que quiere mostrar o no las consultas a la bd
);
