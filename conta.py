
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