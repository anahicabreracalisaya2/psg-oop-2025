
class Gato:
    def __init__(self, color):
        self.color = color


pantera = Gato("negro")
snowball = Gato("blanco")
print(pantera.color)
print(snowball.color)
pantera = Gato("negro")
snowball = Gato("blanco")

class Gato:
    especie = "felino"
    def __init__(self, color):
        self.color = color
pantera = Gato("negro")
snowball = Gato("blanco")
print(pantera.especie, pantera.color)
print(snowball.especie, snowball.color)
# Atributo de clase
print(Gato.especie)