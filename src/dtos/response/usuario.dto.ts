import { Exclude, Expose } from "class-transformer";
import { TipoUsuario } from "../../models/usuarios.model";

@Exclude()
export class UsuarioDto {
  @Expose()
  usuarioId: string;

  @Expose()
  usuarioNombre: string;

  @Expose()
  usuarioTipo: TipoUsuario;

  @Expose()
  usuarioFoto?: string;

  @Expose()
  usuarioCorreo: string;

  @Expose()
  usuarioJwt: string;

  usuarioPassword: string;
}
