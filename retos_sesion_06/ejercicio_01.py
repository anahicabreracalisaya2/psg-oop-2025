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
        self.indica_parada = 0      # índice de la parada actual
        self.sentido = 1            # 1 = ida, -1 = vuelta

    def parada_actual(self):
        return self.paradas[self.indica_parada]

    def mover(self):
        """Avanza a la siguiente parada e invierte sentido si llega al final."""
        self.indica_parada += self.sentido
        if self.indica_parada == len(self.paradas):
            self.sentido = -1
            self.indica_parada = len(self.paradas) - 2

        elif self.indica_parada < 0:
            self.sentido = 1
            self.indica_parada = 1

        print(f"\n🚌 El minibús llegó a la parada: {self.parada_actual()}")

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
            print(f"⬇️ {p.nombre} ha bajado en {parada}.")
            self.pasajeros.remove(p)

    def mostrar_pasajeros(self):
        print(f"\n🚌 Minibús Ruta {self.ruta} - Parada actual: {self.parada_actual()}")
        if not self.pasajeros:
            print("No hay pasajeros a bordo.")
        else:
            print("Pasajeros a bordo:")
            for p in self.pasajeros:
                p.info()

minibus = Minibus("381", ["Arce", "Prado", "Perez"])

p1 = Pasajero("Saul", "Prado")
p2 = Pasajero("Amanda", "Perez")
p3 = Pasajero("Samuel", "Camacho")

print("\nSubiendo pasajeros:")
minibus.subir_pasajero(p1)
minibus.subir_pasajero(p2)
minibus.subir_pasajero(p3)

print("\nEstado del minibús:")
minibus.mostrar_pasajeros()

print("\nRecorrido del minibús:")
for i in range(6):
    minibus.mover()
    minibus.bajar_pasajeros()
    minibus.mostrar_pasajeros()