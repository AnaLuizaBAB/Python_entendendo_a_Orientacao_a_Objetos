class Conta():


    def __init__(self, conta, titular, saldo, limite):
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato (self):
        return self.__saldo
    
    def deposito (self, valor):
        self.__saldo += valor
    
    def saque (self, valor):
        self.__saldo -= valor

    def tranfere (self, valor, conta_destino):
        self.saque(valor)
        conta_destino.deposito(valor)


    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def get_titular(self):
        return self.__titular


    def set_limite(self, novo_limite):
        self.__limite = novo_limite