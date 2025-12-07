# Encapsulación
# Autor: Jenifer Fernanda Vaca Escobar

class CuentaBancaria:

    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(30)
print("Saldo final:", cuenta.obtener_saldo())