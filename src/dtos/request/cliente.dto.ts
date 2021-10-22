import {
  IsEmail,
  IsNotEmpty,
  IsString,
  MaxLength,
  MinLength,
} from "class-validator";
import { BaseDto } from "../base.dto";

export class ClienteDto extends BaseDto {
  @IsString()
  @IsNotEmpty()
  clienteNombre: string;

  @IsString()
  @IsNotEmpty()
  clienteApellido: string;

  @IsEmail()
  @IsNotEmpty()
  clienteCorreo: string;

  @IsString()
  @MaxLength(9, { message: "El DNI es 8 caracteres" })
  @MinLength(7, { message: "El DNI es 8 caracteres" })
  clienteDni: string;
}
