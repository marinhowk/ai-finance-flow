from models.user_model import Usuarios

class UsuariosController:
    def __init__(self, db):
        self.conn = db.get_conexao()
        self.cursor = self.conn. cursor()

    def login():
        pass

    def cadastro(self, usuario: Usuarios, email_verificado):
        query = """
        INSERT INTO usuarios (nome, email, senha, email_verificado)
        VALUES (%s, %s, %s, %s)
        """

        valores = (usuario.nome, usuario.email, usuario.senha, email_verificado)
        self.cursor.execute(query, valores)
        self.conn.commit()
