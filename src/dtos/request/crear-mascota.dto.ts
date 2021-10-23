import { IsDateString, IsEnum, IsNotEmpty, IsString } from "class-validator";
import { BaseDto } from "../base.dto";

export enum MascotaSexo {
  MACHO = "MACHO",
  HEMBRA = "HEMBRA",
}

export class crearMascotaDto extends BaseDto {
  @IsString()
  @IsNotEmpty()
  mascotaNombre: string;

  @IsString()
  @IsNotEmpty()
  mascotaRaza: string;

  @IsEnum(MascotaSexo, {
    message: "MascotaSexo solo tiene valores 'MACHO' | 'HEMBRA'",
  })
  @IsNotEmpty()
  mascotaSexo: MascotaSexo;

  @IsDateString()
  @IsNotEmpty()
  mascotaFechaNacimiento: Date;

  @IsString()
  @IsNotEmpty()
  clienteId: string;
}
