import mysql.connector

class ReclamacaoRepository:

    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'ouvidoriadatabase'
    )
                
    cursor = connection.cursor()

    def __int__(self):
        pass

    def findAllReclamacao(self):
        sql = 'select * from tb_reclamacao'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findReclamacaoByUsuarioId(self, idUsuario):
        sql = f'select * from tb_reclamacao where usuario_id = {idUsuario}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def findReclamacaoById(self, id):
        sql = f'select * from tb_reclamacao where id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveReclamacao(self, reclamacao, idUsuario):
        sql = f'insert into tb_reclamacao (reclamacao, usuario_id) values ("{reclamacao}", {idUsuario})'
        self.cursor.execute(sql)

    def deleteReclamacaoById(self, id):
        sql = f'delete from tb_reclamacao where id = {id}'
        self.cursor.execute(sql)

    def deleteAllReclamacao(self):
        sql = 'truncate table tb_reclamacao'
        self.cursor.execute(sql)

    def closerCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()