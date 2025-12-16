class Cuenta:
    def __init__(self, nombre_titular):
        self.__numero_cuenta = "123567901"
        self.__saldo = 0
        self.nombre_titular = nombre_titular

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
    def saldo(self):
        print(f"💵 Su saldo actual es: {self.__saldo}")
        return self.__saldo
    def numero_cuenta(self):
        print(f"🔢 Su número de cuenta es: {self.__numero_cuenta}")
        return self.__numero_cuenta
    def nombre_titular(self):
        print(f"👤 Titular de la cuenta: {self.nombre_titular}")
        return self.nombre_titular
    def cambio_titular(self, nuevo_nombre):
        if self.nombre_titular != nuevo_nombre:
            self.nombre_titular = nuevo_nombre
            print("✅ Nombre del titular actualizado correctamente.")
        else:
            print("⚠️ Nombre inválido. No se realizaron cambios.")




# Implementando la clase
cuenta = Cuenta("Anahi Cabrera")
print("Informaciom de la cuenta:")
print("Número de cuenta:", cuenta.numero_cuenta)
print("Titular:", cuenta.nombre_titular)
print("Saldo inicial:", cuenta.saldo)
cuenta.depositar(200)
cuenta.retirar(100)
cuenta.retirar(700)  # Error
print("Cambiando de titular...")
cuenta.cambio_titular("Cielo Calisaya")
print("Nuevo titular:", cuenta.nombre_titular)
