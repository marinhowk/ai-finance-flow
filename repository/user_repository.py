from models.user_model import Usuarios

class UsuariosRepository:
    def __init__(self, db):
        self.conn = db.get_conexao()
        self.cursor = self.conn.cursor()

    def salvar_cadastro(self, usuario: Usuarios):
        query = """
        INSERT INTO usuarios (nome, email, senha)
        VALUES (%s, %s, %s)
        """

        valores = (usuario.nome, usuario.email, usuario.senha)
        self.cursor.execute(query, valores)
        self.conn.commit()