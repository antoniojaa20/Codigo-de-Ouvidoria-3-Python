import mysql.connector

class ElogioRepository:

    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'ouvidoriadatabase'
    )
                
    cursor = connection.cursor()

    def __int__(self):
        pass

    def findAllElogio(self):
        sql = 'select * from tb_elogio'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def findElogioByUsuarioId(self, idUsuario):
        sql = f'select * from tb_elogio where usuario_id = {idUsuario}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findElogioById(self, id):
        sql = f'select * from tb_elogio where id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveElogio(self, elogio, idUsuario):
        sql = f'insert into tb_elogio (elogio, usuario_id) values ("{elogio}", {idUsuario})'
        self.cursor.execute(sql)

    def deleteElogioById(self, id):
        sql = f'delete from tb_elogio where id = {id}'
        self.cursor.execute(sql)

    def deleteAllElogio(self):
        sql = 'truncate table tb_elogio'
        self.cursor.execute(sql)

    def closerCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()