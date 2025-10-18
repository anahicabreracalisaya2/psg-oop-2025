class Celula:
    def __init__(self, ADN, tipo_celula, energia_inicial):
        self.__ADN = ADN
        self.__energia = energia_inicial
        self._tipo_celula = tipo_celula

    @property
    def ADN(self):
        return self.__ADN

    @property
    def tipo_celula(self):
        return self._tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        if self._tipo_celula != nuevo_tipo:
            self._tipo_celula = nuevo_tipo
            print(f"🧫 Tipo de célula modificado a: {self._tipo_celula}")
        else:
            print("⚠️ Tipo de célula inválido. No se realizaron cambios.")

    @property
    def energia(self):
        return self.__energia

    def comer(self, cantidad):
        if cantidad > 0:
            self.__energia += cantidad
            print(f"🍽️ La célula ha comido. Energía actual: {self.__energia}")
        else:
            print("⚠️ La cantidad de energía a ingerir debe ser positiva.")

    def dividirse(self):
        costo_division = 50
        if self.__energia >= costo_division:
            self.__energia -= costo_division
            print(f"🧬 La célula se ha dividido. Energía restante: {self.__energia}")
        else:
            print("❌ Energía insuficiente para dividirse.")

    def __str__(self):
        return (f"🧫 Célula tipo: {self.tipo_celula}\n"
                f"ADN: {self.ADN}\n"
                f"Energía: {self.energia}")

# Implementando la clase

celula1 = Celula("ABC123", "epitelial", 120)
print(celula1)
print("ADN:", celula1.ADN)
print("Tipo:", celula1.tipo_celula)
print("Energía:", celula1.energia)
celula1.tipo_celula = "muscular"
celula1.comer(30)
celula1.dividirse()
celula1.dividirse()  