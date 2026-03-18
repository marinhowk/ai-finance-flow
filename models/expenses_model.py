from datetime import date
from decimal import Decimal

class Gastos:
    def __init__(self, descricao, categoria, metodo_pagamento, quantidade_parcelas, vencimento: date, valor: Decimal, status, tipo):
        self.descricao = descricao
        self.categoria = categoria
        self.metodo_pagamento = metodo_pagamento
        self.quantidade_parcelas = quantidade_parcelas
        self.vencimento = vencimento
        self.valor = valor
        self.status = status
        self.tipo = tipo

    