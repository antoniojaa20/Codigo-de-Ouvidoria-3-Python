from repositories import ReclamacaoRepository

class ReclamacaoService:
    ReclamacaoRepository = ReclamacaoRepository.ReclamacaoRepository()

    def __init__(self):
        pass

    def findAllReclamacao(self):
        reclamacao = self.ReclamacaoRepository.findAllReclamacao()
        self.ReclamacaoRepository.commit()
        return reclamacao

    def findReclamacaoByUsuarioId(self, idUsuario):
        reclamacao = self.ReclamacaoRepository.findReclamacaoByUsuarioId(idUsuario=idUsuario)
        self.ReclamacaoRepository.commit()
        return reclamacao

    def findReclamacaoById(self, id):
        reclamacao = self.ReclamacaoRepository.findReclamacaoById(id=id)
        self.ReclamacaoRepository.commit()
        return reclamacao

    def saveReclamacao(self, reclamacao, idUsuario):
        self.ReclamacaoRepository.saveReclamacao(reclamacao=reclamacao, idUsuario=idUsuario)
        self.ReclamacaoRepository.commit()
        

    def deleteReclamacaoById(self, id):
        self.ReclamacaoRepository.deleteReclamacaoById(id=id)
        self.ReclamacaoRepository.commit()
        

    def deleteAllReclamacao(self):
        self.ReclamacaoRepository.deleteAllReclamacao()
        self.ReclamacaoRepository.commit()