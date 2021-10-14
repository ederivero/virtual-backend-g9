import { DataTypes } from "sequelize";
import conexion from "../config/sequelize";
// import { v4 } from "uuid"; // yarn add uuid
// yarn add --dev @types/uuid

// cuando hacemos una exportacion por defecto, esta no puede llevar la asignacion de una variable, es decir solamente debe llevar el contenido que tendria dicha variable
// solamente se podra hacer un export default nombre_variable cuando la hallamos definido previamente

export default () =>
  conexion.define(
    "producto",
    {
      productoId: {
        primaryKey: true,
        type: DataTypes.UUID,
        defaultValue: DataTypes.UUIDV4,
        field: "id",
      },
      productoNombre: {
        type: DataTypes.STRING(100),
        allowNull: false,
        field: "nombre",
      },
      productoPrecio: {
        type: DataTypes.DECIMAL(5, 2),
        allowNull: false,
        field: "precio",
      },
      productoCantidad: {
        type: DataTypes.INTEGER,
        allowNull: false,
        field: "cantidad",
      },
      productoFoto: {
        type: DataTypes.ARRAY(DataTypes.TEXT),
        allowNull: true,
        field: "foto",
      },
    },
    {
      tableName: "productos",
      timestamps: false,
    }
  );
