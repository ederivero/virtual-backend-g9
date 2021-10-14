import { DataTypes } from "sequelize";
import conexion from "../config/sequelize";
import { hashSync } from "bcrypt";

export enum TipoUsuario {
  ADMIN = "ADMIN",
  CLIENTE = "CLIENTE",
}

export default () =>
  conexion.define(
    "usuario",
    {
      usuarioId: {
        type: DataTypes.UUID,
        primaryKey: true,
        defaultValue: DataTypes.UUIDV4,
        field: "id",
      },
      usuarioNombre: {
        type: DataTypes.STRING(40),
        field: "nombre",
        allowNull: false,
      },
      usuarioCorreo: {
        type: DataTypes.STRING(40),
        field: "correo",
        validate: {
          isEmail: true,
        },
        allowNull: false,
        unique: true,
      },
      usuarioPassword: {
        type: DataTypes.TEXT,
        field: "password",
        allowNull: false,
        set(valor: string) {
          // aca encriptaremos la password
          // convertira el valor puro y en base al numero de vueltas lo combinara con un salt y a medida que haya mas vueltas mas dificil sera de encontrar el valor inicial
          const passwordEncriptada = hashSync(valor, 10);
          // sirve para modificar en esa misma instancia de la creacion del registro modificar el valor de una de las columnas
          // nombre que le ponemos a la columna en el ORM, valor a modificar
          this.setDataValue("usuarioPassword", passwordEncriptada);
        },
      },
      usuarioTipo: {
        type: DataTypes.ENUM(TipoUsuario.ADMIN, TipoUsuario.CLIENTE),
        field: "tipo",
        defaultValue: TipoUsuario.CLIENTE,
      },
      usuarioFoto: {
        type: DataTypes.TEXT,
        field: "foto",
      },
    },
    {
      tableName: "usuarios",
      timestamps: false,
    }
  );
