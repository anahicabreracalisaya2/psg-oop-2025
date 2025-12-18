from random import choice
OPCIONES = ["piedra", "papel", "tijera"]
class Computadora:
    def __init__(self):
        self.nombre = "Computadora"
 
    def __str__(self):
        return self.nombre
    
    def elegir(self):
        return choice(OPCIONES)