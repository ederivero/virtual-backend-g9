import { IsDateString, IsEnum, IsOptional, IsString } from "class-validator";
import { BaseDto } from "../base.dto";
import { MascotaSexo } from "./crear-mascota.dto";

export class actualizarMascotaDto extends BaseDto {
  @IsString()
  @IsOptional()
  mascotaNombre?: string;

  @IsString()
  @IsOptional()
  mascotaRaza?: string;

  @IsEnum(MascotaSexo)
  @IsOptional()
  mascotaSexo?: MascotaSexo;

  @IsDateString()
  @IsOptional()
  mascotaFechaNacimiento?: Date;
}
