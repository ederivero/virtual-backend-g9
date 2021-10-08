import { DataTypes } from "sequelize";
import { conexion } from "../config/sequelize";

// https://sequelize.org/master/manual/model-basics.html#column-options

export const tareaModel = () =>
  conexion.define(
    "tarea",
    {
      tareaId: {
        primaryKey: true, // si sera la columna primary key
        unique: true, // si puede ser unique
        autoIncrement: true, // si va a ser la columna autoincrementable
        allowNull: false, // si puede permitir valores nulos
        field: "id", // el nombre de la columna en la bd
        type: DataTypes.INTEGER, // tipo de dato en la bd
      },
      tareaNombre: {
        type: DataTypes.STRING(50),
        field: "nombre",
        allowNull: false,
      },
      tareaHora: {
        type: DataTypes.TIME,
        field: "hora",
        allowNull: true,
      },
      tareaDias: {
        type: DataTypes.ARRAY(
          DataTypes.ENUM(["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"])
        ),
        field: "dias",
        allowNull: true,
      },
    },
    {
      tableName: "tareas",
      timestamps: true, // crear los campos de createdAt y updatedAt para que cuando se cree o se actualice un registro se ponga la fecha en la cual se esta haciendo la modificacion
      updatedAt: "fecha_de_actualizacion",
    }
  );
