from models.Usuario import UsuarioModel
from bcrypt import checkpw
from .conexion_bd import base_de_datos


class Usuario:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __str__(self):
        return "Usuario con el id='%s' y username = '%s'" % (self.id, self.username)
        # return "Usuario con el id='{}' y username = '{}'".format(self.id, self.username)


def autenticador(username, password):
    '''Funcion encargada en mi JWT de validar las credenciales, valida si son ingresadas correctamente y luego valida si es el usuario'''
    if username and password:
        # buscamos el usuario en la base de datos segun el correo
        usuario = base_de_datos.session.query(UsuarioModel).filter(
            UsuarioModel.usuarioCorreo == username).first()
        # si hay un usuario
        if usuario:
            # validamos su password
            hash = bytes(usuario.usuarioPassword, 'utf-8')
            pwdBytes = bytes(password, 'utf-8')
            if checkpw(pwdBytes, hash) is True:
                print('Es el usuario')
                return Usuario(usuario.usuarioId, usuario.usuarioCorreo)
    return None


def identificador(payload):
    '''Sirve para que una vez el usuario envie la token y quiera realizar una peticion a una ruta protegida esta funcion sera encargada de identificar a dicho usuario y devolver su informacion'''
    print(payload)
    usuarioId = payload.get('identity')
    usuarioEncontrado = base_de_datos.session.query(
        UsuarioModel).filter(UsuarioModel.usuarioId == usuarioId).first()
    if usuarioEncontrado:
        return usuarioEncontrado.__dict__
    return None
