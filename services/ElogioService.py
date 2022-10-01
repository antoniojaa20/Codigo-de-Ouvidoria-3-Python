from repositories import ElogioRepository

class ElogioService:
    ElogioRepository = ElogioRepository.ElogioRepository()

    def __init__(self):
        pass

    def findAllElogio(self):
        elogio = self.ElogioRepository.findAllElogio()
        self.ElogioRepository.commit()
        return elogio

    def findElogioByUsuarioId(self, idUsuario):
        elogio = self.ElogioRepository.findElogioByUsuarioId(idUsuario=idUsuario)
        self.ElogioRepository.commit()
        return elogio

    def findElogioById(self, id):
        elogio = self.ElogioRepository.findElogioById(id=id)
        self.ElogioRepository.commit()
        return elogio

    def saveElogio(self, elogio, idUsuario):
        self.ElogioRepository.saveElogio(elogio=elogio, idUsuario=idUsuario)
        self.ElogioRepository.commit()
        

    def deleteElogioById(self, id):
        self.ElogioRepository.deleteElogioById(id=id)
        self.ElogioRepository.commit()
        

    def deleteAllElogio(self):
        self.ElogioRepository.deleteAllElogio()
        self.ElogioRepository.commit()