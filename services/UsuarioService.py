from repositories import UsuarioRepository

class UsuarioService:
    UsuarioRepository = UsuarioRepository.UsuarioRepository()

    def __init__(self):
        pass

    def findAllUsuarios(self):
        usuarios = self.UsuarioRepository.findAllUsuarios()
        self.UsuarioRepository.commit()
        return usuarios

    def findUsuarioById(self, id):
        usuario = self.UsuarioRepository.findUsuarioById(id=id)
        self.UsuarioRepository.commit()
        return usuario

    def findUserbyUsuario(self, usuario):
        usuario = self.UsuarioRepository.findUserbyUsuario(usuario=usuario)
        self.UsuarioRepository.commit()
        return usuario

    def saveUsuario(self, nome, usuario, senha):
        self.UsuarioRepository.saveUsuario(nome=nome, usuario=usuario, senha=senha)
        self.UsuarioRepository.commit()
        

    def deleteUsuarioById(self, id):
        self.UsuarioRepository.deleteUsuarioById(id=id)
        self.UsuarioRepository.commit()
        

    def deleteAllUsuarios(self):
        self.UsuarioRepository.deleteAllUsuairios()
        self.UsuarioRepository.commit()