import {
  IsEmail,
  IsEnum,
  IsNotEmpty,
  IsOptional,
  IsString,
  Length,
  Matches,
} from "class-validator";
import { TipoUsuario } from "../../models/usuarios.model";

export class RegistroDto {
  @IsString()
  @IsNotEmpty()
  usuarioNombre: string;

  @IsEmail()
  @IsNotEmpty()
  usuarioCorreo: string;

  @IsString()
  @Matches(
    /(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}/,
    {
      message:
        "Password invalida, debe de ser al menos una mayus, una minus, un numero y un caracter especial y no menor de 6 caracteres",
    }
  )
  @IsNotEmpty()
  usuarioPassword: string;

  @IsEnum(TipoUsuario)
  @IsOptional()
  usuarioTipo?: TipoUsuario;

  @IsOptional()
  @IsString()
  usuarioFoto?: string;
}
