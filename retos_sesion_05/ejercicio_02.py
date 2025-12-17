class Nadador:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def nadar(self):
        print("Este personaje está nadando 🏊‍♂️")
    def mostrar(self):
        print(f"Habilidad: {self.habilidad}")


class Volador:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def volar(self):
        print("Este personaje está volando 🕊️")
    def mostrar(self):
        print(f"Habilidad: {self.habilidad}")


class Pez(Nadador):
    def __init__(self, habilidad, tipo):
        super().__init__(habilidad)
        self.tipo = tipo
    def mostrar(self):
        super().mostrar()
        print(f"Tipo: {self.tipo}")
        self.nadar()


class Pajaro(Volador):
    def __init__(self, habilidad, tipo):
        super().__init__(habilidad)
        self.tipo = tipo
    def mostrar(self):
        super().mostrar()
        print(f"Tipo: {self.tipo}")
        self.volar()


class Pato(Nadador, Volador):
    def __init__(self, habilidad, tipo):
        super().__init__(habilidad)  # Llama al constructor de Nadador
        self.tipo = tipo
    def mostrar(self):
        super().mostrar()  # Llama a mostrar() de Nadador por MRO
        print(f"Tipo: {self.tipo}")
        self.nadar()       # El pato nada
        self.volar()       # Y también vuela


# Aplicación
pez = Pez("rápido", "de agua dulce")
pajaro = Pajaro("planeado", "de rapiña")
pato = Pato("calmado", "silvestre")

pez.mostrar()
pajaro.mostrar()
pato.mostrar()