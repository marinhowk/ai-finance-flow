from models.user_model import Usuarios
from repository.user_repository import UsuariosRepository
from config.database import BancoDeDados
from services.email_service import enviar_email
import random

db = BancoDeDados()
ur = UsuariosRepository(db)

class UsuariosController:

    def reliazar_login(self, email, senha):
        usuario = ur.buscar_email(email)

        if not usuario:
            return {
                "status" : "erro",
                "mensagem" : "E-mail e/ou senha inválidos."
            }
        else:
            Usuarios.validar_senha(senha, usuario["senha"])

            return {
                "status" : "ok",
                "mensagem" : "Login realizado com sucesso."
            }
        
    def validar_dados (self, nome, email, senha, confirmar_senha):
        if not nome or not email or not senha or not confirmar_senha:
            return {
                "status" : "erro",
                "mensagem" : "Todos os campos são obrigatórios."
            }
        
        elif senha != confirmar_senha:
            return {
                "status" : "erro",
                "mensagem" : "As senhas informadas são diferentes."
            }
        
        else:
            return {
                "status" : "ok"
            }
         
    def gerar_codigo(self):
        return random.randint(1000, 9999)
    
    def enviar_email(self, email):
        self.codigo_gerado = self.gerar_codigo()
        enviar_email(email, self.codigo_gerado)

    def validar_codigo(self, codigo):

        if str(codigo).strip() == str(self.codigo_gerado):
            return {
                "status" : "ok",
                "mensagem" : "Código informado corretamente."
            }
        
        else:
            return {
                "status" : "erro",
                "mensagem" : "Código inválido, tente novamente."
            }
        
        
    
