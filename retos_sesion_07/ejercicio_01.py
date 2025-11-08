class Herramienta:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

class Martillo(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🔨 El martillo se usa para clavar clavos.")
        print(f"Tiene un tipo de Mango: {self.tipo_mango}, con un Material: {self.material}, y un Peso: {self.peso} kg\n")


class Destornillador(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🪛 El destornillador se usa para ajustar tornillos.")
        print(f"Tiene un tipo de Mango: {self.tipo_mango}, con un Material: {self.material}, y un Peso: {self.peso} kg\n")


class LlaveInglesa(Herramienta):
    def __init__(self, tipo_mango, material, peso):
        super().__init__(tipo_mango, material, peso)

    def usar(self):
        print("🔧 La llave inglesa se usa para apretar tuercas.")
        print(f"Tiene un tipo de Mango: {self.tipo_mango}, con un Material: {self.material}, y un Peso: {self.peso} kg\n")

class Carpintero:
    def usar_herramienta(self, herramienta: Herramienta):
        herramienta.usar()



juan = Carpintero()

martillo = Martillo("madera", "acero", 2.2)
destornillador = Destornillador("plástico", "acero", 0.8)
llave = LlaveInglesa("goma", "hierro", 1.7)

juan.usar_herramienta(martillo)
juan.usar_herramienta(destornillador)
juan.usar_herramienta(llave)