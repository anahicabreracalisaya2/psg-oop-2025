class Vehiculo:
    def __init__(self, medio):
        self._velocidad = 0  
        self.medio = medio
    def ver_velocidad(self):
        print("La velocidad actual es:", self._velocidad, "km/h")
        return self._velocidad

    def velocidad_cambio(self,accion,valor):
        if accion == "aumentar":
            self._velocidad += valor
        elif accion == "disminuir":
            self._velocidad -= valor
            if self._velocidad < 0:
                self._velocidad = 0

    def ver_medio(self):
        print("El medio de transporte es:", self.medio)
        return self.medio
    
    def cambia_medio(self, nuevo_medio):
        self.medio = nuevo_medio


class Bicicleta(Vehiculo):
    def __init__(self, medio):
        super().__init__(medio)

    def pedalear(self):
        self._velocidad += 5
        print("Se encuentra pedaleando 🚴‍♀️... la velocidad aumentada en 5 km/h")

    
class Avion(Vehiculo):
    def __init__(self, medio):
        super().__init__(medio)

    def volar(self):
        self._velocidad += 50
        print("Esta volando ✈️... La velocidad aumentada en 50 km/h")

   


# Uso
print("Bicicleta:")
bici = Bicicleta("Terrestre")
bici.ver_medio()
bici.pedalear()
bici.ver_velocidad()
bici.velocidad_cambio("aumentar", 22)
bici.ver_velocidad()
print("\nAvion:")
avion = Avion("Aéreo")
avion.ver_medio()   
avion.volar()
avion.ver_velocidad()
avion.velocidad_cambio("aumentar", 150)
avion.velocidad_cambio("disminuir", 100)
avion.ver_velocidad()
avion.cambia_medio("Terrestre")
avion.ver_medio()


