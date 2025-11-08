# Clase base
class Herramienta:
    def __init__(self, tipo_mango, material, peso):
        self.tipo = "manual"
        self.energia = "fuerza humana"
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

    def usar(self):
        print(f"Herramienta manual con mango de {self.tipo_mango}")
        print(f"Material: {self.material}, Peso: {self.peso} kg")
        print(f"Funciona con {self.energia}")


# Subclases especializadas
class Martillo(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🔨 El martillo se usa para clavar clavos.")
        print(f"Tipo: {self.tipo}, Energía: {self.energia}")
        print(f"Mango: {self.tipo_mango}, Material: {self.material}, Peso: {self.peso} kg\n")


class Destornillador(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🪛 El destornillador se usa para ajustar tornillos.")
        print(f"Tipo: {self.tipo}, Energía: {self.energia}")
        print(f"Mango: {self.tipo_mango}, Material: {self.material}, Peso: {self.peso} kg\n")


class LlaveInglesa(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🔧 La llave inglesa se usa para apretar tuercas.")
        print(f"Tipo: {self.tipo}, Energía: {self.energia}")
        print(f"Mango: {self.tipo_mango}, Material: {self.material}, Peso: {self.peso} kg\n")


# Clase Carpintero
class Carpintero:
    def usar_herramienta(self, herramienta: Herramienta):
        herramienta.usar()


# Ejemplo de uso sin if ni for
juan = Carpintero()

martillo = Martillo("madera", "acero", 1.2)
destornillador = Destornillador("plástico", "acero", 0.4)
llave = LlaveInglesa("goma", "hierro", 0.9)

juan.usar_herramienta(martillo)
juan.usar_herramienta(destornillador)
juan.usar_herramienta(llave)