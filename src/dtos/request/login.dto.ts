import { IsEmail, IsNotEmpty, IsString } from "class-validator";

export class LoginDto {
  @IsEmail()
  @IsNotEmpty()
  correo: string;

  @IsString()
  @IsNotEmpty()
  password: string;
}
