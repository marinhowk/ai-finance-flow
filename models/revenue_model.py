from datetime import date 
from decimal import Decimal

class Receitas:
    def __init__(self, origem, data_recebimento: date, valor: Decimal, status):
        self.origem = origem
        self.data_recebimento = data_recebimento
        self.valor = valor
        self.status = status
        