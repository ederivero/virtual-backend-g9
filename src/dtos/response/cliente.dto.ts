import { Exclude, Expose } from "class-transformer";

@Exclude()
export class ClienteDto {
  @Expose()
  _id: string;

  @Expose()
  clienteNombre: string;

  @Expose()
  clienteApellido: string;

  @Expose()
  clienteCorreo: string;

  @Expose()
  clienteDni: string;

  fecha_creacion: Date;

  __v: number;
}
