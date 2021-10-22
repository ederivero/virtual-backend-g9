import { model, Schema } from "mongoose";

interface ICliente {
  clienteNombre: string;
  clienteApellido: string;
  clienteCorreo: string;
  clienteDni: string;
}

const clienteSchema = new Schema<ICliente>(
  {
    clienteNombre: {
      type: Schema.Types.String,
      alias: "nombre", // sera el nombre con el que se guarada las llaves en los documentos
      required: true,
      maxlength: 40,
    },
    clienteApellido: {
      type: Schema.Types.String,
      alias: "apellido",
      required: true,
    },
    clienteCorreo: {
      type: Schema.Types.String,
      validate: {
        validator: (input: string) => /\w+[@]\w+[.]\w{2,3}/.test(input),
        message: "El valor no es un correo",
      },
    },
    clienteDni: {
      type: Schema.Types.String,
      maxlength: 8,
      minlength: [8, "El valor minimo es 8"],
    },
  },
  { timestamps: { createdAt: "fecha_creacion", updatedAt: false } }
);

const Cliente = model<ICliente>("clientes", clienteSchema);

export default Cliente;
