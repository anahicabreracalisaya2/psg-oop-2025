class Vehiculo:
    def __init__(self, medio):
        self._velocidad = 0  
        self.medio = medio

    def get_velocidad(self):
        return self._velocidad

    def set_medio(self, nuevo_medio):
        self.medio = nuevo_medio

    def mostrar(self):
        print(f"Medio: {self.medio}")
        print(f"Velocidad: {self._velocidad} km/h")


class Bicicleta(Vehiculo):
    def __init__(self, medio):
        super().__init__(medio)

    def pedalear(self):
        self._velocidad += 5
        print("Se encuentra pedaleando 🚴‍♀️... la velocidad aumentada en 5 km/h")

    def mostrar(self):
        super().mostrar()
        self.pedalear()


class Avion(Vehiculo):
    def __init__(self, medio):
        super().__init__(medio)

    def volar(self):
        self._velocidad += 50
        print("Esta volando ✈️... La velocidad aumentada en 50 km/h")

    def mostrar(self):
        super().mostrar()
        self.volar()


# Uso
print("Bicicleta:")
bici = Bicicleta("Terrestre")
bici.mostrar()
bici.set_medio("Montaña")
print(f"Velocidad actual: {bici.get_velocidad()} km/h")

print("Avión:")
avion = Avion("Aereo")
avion.mostrar()
print(f"Nuevo medio: {avion.medio}")
print(f"Velocidad actual: {avion.get_velocidad()} km/h")

# isinstance()
print("¿bici es Bicicleta?", isinstance(bici, Bicicleta))
print("¿bici es Vehiculo?", isinstance(bici, Vehiculo))
print("¿bici es Avion?", isinstance(bici, Avion))

# issubclass()
print("¿Bicicleta es Vehiculo?", issubclass(Bicicleta, Vehiculo))
print("¿Avion es Vehiculo?", issubclass(Avion, Vehiculo))
print("¿Avion es Bicicleta?", issubclass(Avion, Bicicleta))