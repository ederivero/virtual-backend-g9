import { Schema } from "mongoose";

interface IMascota {
  mascotaNombre: string;
  mascotaRaza: string;
  mascotaSexo: "MACHO" | "HEMBRA";
  mascotaFechaNacimiento: Date;
}

export const mascotaSchema = new Schema<IMascota>(
  {
    mascotaNombre: {
      type: Schema.Types.String,
      alias: "nombre",
    },
    mascotaRaza: {
      type: Schema.Types.String,
      alias: "raza",
    },
    mascotaSexo: {
      type: Schema.Types.String,
      enum: ["MACHO", "HEMBRA"],
      alias: "sexo",
    },
    mascotaFechaNacimiento: {
      type: Schema.Types.Date,
      alias: "fecha_nac",
    },
  },
  {
    timestamps: false,
  }
);
