import hashlib

class Users:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self._senha_hash(senha)

    def _senha_hash(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @staticmethod
    def validar_senha(senha_digitada, senha_banco):
        senha_hash = hashlib.sha256(senha_digitada.encode()).hexdigest()
        return senha_hash == senha_banco
    
    @staticmethod
    def redefinir_senha(nova_senha):
        return hashlib.sha256(nova_senha.encode()).hexdigest()