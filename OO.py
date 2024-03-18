
class Conta():


    def __init__(self, conta, titular, saldo, limite):
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def extrato (self):
        return self.saldo
    
    def deposito (self, valor):
        self.saldo += valor
    
    def saque (self, valor):
        self.saldo -= valor