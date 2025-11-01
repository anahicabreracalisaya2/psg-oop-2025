class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def info(self):
        print(f"Pasajero: {self.nombre}, Destino: {self.destino}")


class Minibus:
    def __init__(self, ruta, paradas):
        self.ruta = ruta
        self.paradas = paradas
        self.pasajeros = []
        self.indica_parada = 0
        self.direccion = 1  # 1: adelante, -1: atrás

    def parada_actual(self):
        return self.paradas[self.indica_parada]

    def mover(self):
        self.indica_parada += self.direccion
        if self.indica_parada >= len(self.paradas) or self.indica_parada < 0:
            self.direccion *= -1
            self.indica_parada += self.direccion * 2  # retroceder dos pasos

    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.paradas:
            self.pasajeros.append(pasajero)
            print(f"✅ {pasajero.nombre} ha subido al minibús.")
        else:
            print(f"❌ {pasajero.nombre} no puede subir. Su destino no está en la ruta.")

    def bajar_pasajeros(self):
        parada = self.parada_actual()
        bajan = [p for p in self.pasajeros if p.destino == parada]
        for p in bajan:
            print(f" {p.nombre} ha bajado en {parada}.")
            self.pasajeros.remove(p)

    def mostrar_pasajeros(self):
        print(f" Minibús Ruta {self.ruta} - Parada actual: {self.parada_actual()}")
        if not self.pasajeros:
            print("No hay pasajeros a bordo.")
        else:
            for p in self.pasajeros:
                p.info()

# Uso del Ejercicio
minibus = Minibus("381", ["Arce", "Prado", "Perez"])
p1 = Pasajero("Saul", "Prado")
p2 = Pasajero("Amanda", "Perez")
p3 = Pasajero("Samuel", "Camacho")

print("\nSubiendo pasajeros:")
minibus.subir_pasajero(p1)
minibus.subir_pasajero(p2)
minibus.subir_pasajero(p3)
print("\nEstado  del minibús:")
minibus.mostrar_pasajeros()

print("\nRecorrido del minibús:")
for i in range(4):
    minibus.mover()
    minibus.bajar_pasajeros()
    minibus.mostrar_pasajeros()