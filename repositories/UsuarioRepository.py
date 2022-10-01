import mysql.connector

class UsuarioRepository:

    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'ouvidoriadatabase'
    )
                
    cursor = connection.cursor()

    def __int__(self):
        pass

    def findAllUsuarios(self):
        sql = 'select * from tb_usuario'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findUsuarioById(self, id):
        sql = f'select * from tb_usuario where id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findUserbyUsuario(self, usuario):
        sql = f'select * from tb_usuario where usuario = "{usuario}"'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveUsuario(self, nome, usuario, senha):
        sql = f'insert into tb_usuario (nome, usuario, senha) values ("{nome}", "{usuario}", "{senha}")'
        self.cursor.execute(sql)

    def deleteUsuarioById(self, id):
        sql = f'delete from tb_usuario where id = {id}'
        self.cursor.execute(sql)

    def deleteAllUsuairios(self):
        sql = 'truncate table tb_usuario'
        self.cursor.execute(sql)

    def closerCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()