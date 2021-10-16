import { plainToClass } from "class-transformer";
import { validate } from "class-validator";
import { Request, Response } from "express";
import { Usuarios } from "../config/models";
import { RegistroDto } from "../dtos/request/registro.dto";
import { UsuarioDto } from "../dtos/response/usuario.dto";
import { sign, SignOptions } from "jsonwebtoken";
import { TipoUsuario } from "../models/usuarios.model";
import { LoginDto } from "../dtos/request/login.dto";
import { compareSync } from "bcrypt";
import { RequestUser } from "../middlewares/validator";

interface Payload {
  usuarioNombre: string;
  usuarioId: string;
  usuarioFoto?: string;
  usuarioTipo: TipoUsuario;
}

const tokenOptions: SignOptions = {
  expiresIn: "1h",
};

export const registroController = async (req: Request, res: Response) => {
  try {
    const { body } = req;

    const data = plainToClass(RegistroDto, body);
    // este metodo es el encargado de validar en base a los decoradores si los campos cumplen o no cumplen, si no cumple me retornara un array con las observaciones, y si si cumple me retornara un array vacio
    const validacion = await validate(data);

    if (validacion.length !== 0) {
      const mensajes = validacion.map((error) => error.constraints);

      return res.status(400).json({
        content: mensajes,
        message: "Error en los valores",
      });
    }

    const usuarioEncontrado = await Usuarios.findOne({
      where: { usuarioCorreo: body.usuarioCorreo },
    });

    if (usuarioEncontrado) {
      return res.status(400).json({
        content: null,
        message: "Usuario ya existe",
      });
    }

    const nuevoUsuario = await Usuarios.create(body);

    const payload: Payload = {
      usuarioId: nuevoUsuario.getDataValue("usuarioId"),
      usuarioNombre: nuevoUsuario.getDataValue("usuarioNombre"),
      usuarioTipo: nuevoUsuario.getDataValue("usuarioTipo"),
      usuarioFoto: nuevoUsuario.getDataValue("usuarioFoto"),
    };

    const jwt = sign(payload, process.env.JWT_TOKEN ?? "", tokenOptions);
    // Metodo alternativo
    // primero se construye el objeto
    // const nuevoUsuario2 = Usuarios.build({usuarioNombre: 'Eduardo'})
    // nuevoUsuario2.setDataValue('usuarioNombre','asdads')
    // se guarda en la bd
    // await nuevoUsuario2.save()

    const content = plainToClass(UsuarioDto, {
      ...nuevoUsuario.toJSON(),
      usuarioJwt: jwt,
    });
    return res.status(201).json({
      content,
      message: "Usuario creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error,
    });
  }
};

export const login = async (req: Request, res: Response) => {
  //DTO
  const validador = plainToClass(LoginDto, req.body);
  try {
    const resultado = await validate(validador);

    if (resultado.length !== 0) {
      return res.status(400).json({
        content: resultado.map((error) => error.constraints),
        message: "Informacion incorrecta",
      });
    }

    const usuarioEncontrado = await Usuarios.findOne({
      where: { usuarioCorreo: validador.correo },
    });

    if (!usuarioEncontrado) {
      return res.status(400).json({
        message: "Usuario incorrecto",
        content: null,
      });
    }

    const resultado_password = compareSync(
      validador.password,
      usuarioEncontrado.getDataValue("usuarioPassword")
    );

    if (!resultado_password) {
      return res.status(400).json({
        message: "Usuario incorrecto",
        content: null,
      });
    }

    const payload: Payload = {
      usuarioId: usuarioEncontrado.getDataValue("usuarioId"),
      usuarioNombre: usuarioEncontrado.getDataValue("usuarioNombre"),
      usuarioTipo: usuarioEncontrado.getDataValue("usuarioTipo"),
      usuarioFoto: usuarioEncontrado.getDataValue("usuarioFoto"),
    };

    const jwt = sign(payload, process.env.JWT_TOKEN ?? "", tokenOptions);

    return res.json({
      content: jwt,
      message: null,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(400).json({
        message: "error al hace el login",
        content: error.message,
      });
    }
  }
};

export const perfil = (req: RequestUser, res: Response) => {
  const content = plainToClass(UsuarioDto, req.usuario);
  if (!content.usuarioFoto) {
    // content.usuarioNombre => saquen las iniciales EDUARDO DE RIVERO  (ED)
    // MANUEL PEDRO MARTINEZ (MP)
    // split
    // JOSE
    console.log(content.usuarioNombre);
    let [nombre, apellido] = content.usuarioNombre.split(" ");

    content.usuarioFoto = `https://avatars.dicebear.com/api/initials/${
      nombre[0]
    }${apellido ? apellido[0] : undefined}.svg`;
  }
  return res.json({
    message: "Hola desde el endpoint final",
    content,
  });
};

export const actualizarPerfil = (req: RequestUser, res: Response) => {
  // TODO
  // hacer un patch para que el usuario pueda modificar su nombre, su correo, su foto o su contraseña
  // req.usuario = ya tienen toda la info del usuario
};
