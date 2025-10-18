class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular,saldo_ini):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_ini
        self._nombre_titular = nombre_titular

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    @property
    def saldo(self):
        return self.__saldo

    @property
    def nombre_titular(self):
        return self._nombre_titular

    @nombre_titular.setter
    def nombre_titular(self, nuevo_nombre):
        if self._nombre_titular != nuevo_nombre:
            self._nombre_titular = nuevo_nombre
            print("✅ Nombre del titular actualizado correctamente.")
        else:
            print("⚠️ Nombre inválido. No se realizaron cambios.")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"💰 Depósito exitoso. Su nuevo saldo es: {self.__saldo}")
        else:
            print("⚠️ El monto del depósito debe ser mayor a 0 bs.")

    def retirar(self, monto):
        if monto <= 0:
            print("⚠️ El monto a retirar debe ser mayor que cero.")
        elif monto > self.__saldo:
            print("❌ Saldo insuficiente")
        else:
            self.__saldo -= monto
            print(f"🏧 Retiro exitoso. Su saldo es: {self.__saldo}")


# Implementando la clase
cuenta = Cuenta("12345678", "Anahi Cabrera", 500)
print("Número de cuenta:", cuenta.numero_cuenta)
print("Titular:", cuenta.nombre_titular)
print("Saldo inicial:", cuenta.saldo)
cuenta.depositar(200)
cuenta.retirar(100)
cuenta.retirar(700)  # Error
cuenta.nombre_titular = "Cielo Calisaya"
print("Nuevo titular:", cuenta.nombre_titular)
