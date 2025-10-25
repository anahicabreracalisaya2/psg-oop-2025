class Nadador:
    def __init__(self, estilo_nado):
        self.estilo_nado = estilo_nado

    def nadar(self):
        print(f"Nadando con estilo: {self.estilo_nado} 🐠")


class Volador:
    def __init__(self, tipo_vuelo):
        self.tipo_vuelo = tipo_vuelo

    def volar(self):
        print(f"Volando con tipo de vuelo: {self.tipo_vuelo} 🕊️")



class Pez(Nadador):
    def __init__(self, estilo_nado):
        super().__init__(estilo_nado)

    def mostrar(self):
        print("Personaje: Pez")
        print(f"Habilidad: Nadar ({self.estilo_nado})")
        self.nadar()


class Pajaro(Volador):
    def __init__(self, tipo_vuelo):
        super().__init__(tipo_vuelo)

    def mostrar(self):
        print("Personaje: Pájaro")
        print(f"Habilidad: Volar ({self.tipo_vuelo})")
        self.volar()


class Pato(Nadador, Volador):
    def __init__(self, estilo_nado, tipo_vuelo):
        Nadador.__init__(self, estilo_nado)
        Volador.__init__(self, tipo_vuelo)

    def mostrar(self):
        print("Personaje: Pato")
        print(f"Habilidades: Nadar ({self.estilo_nado}) y Volar ({self.tipo_vuelo})")
        self.nadar()
        self.volar()


# Aplicación
pez = Pez("rápido")
pajaro = Pajaro("planeado")
pato = Pato("calmado", "veloz")

print("🐟 PEZ")
pez.mostrar()

print("\n🐦 PÁJARO")
pajaro.mostrar()

print("\n🦆 PATO")
pato.mostrar()
