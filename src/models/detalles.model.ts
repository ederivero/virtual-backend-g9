import { DataTypes } from "sequelize";
import conexion from "../config/sequelize";

export default () =>
  conexion.define(
    "detalles",
    {
      detalleId: {
        primaryKey: true,
        type: DataTypes.UUID,
        defaultValue: DataTypes.UUIDV4,
        field: "id",
      },
      detalleCantidad: {
        field: "cantidad",
        type: DataTypes.INTEGER,
        validate: {
          min: 1,
        },
        allowNull: false,
      },
      detalleTotal: {
        field: "total",
        type: DataTypes.DECIMAL(5, 2),
        allowNull: false,
        validate: {
          min: 0.1,
        },
      },
    },
    {
      tableName: "detalles",
      timestamps: false,
    }
  );
