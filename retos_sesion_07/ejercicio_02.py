class Instrumento:
    def __init__(self, tipo, movimiento):
        self.tipo = tipo
        self.funcion = movimiento
    
    def tocar(self):
        print(f"El instrumento {self.tipo}")
        print(f"Funciona con {self.funcion}")
 
class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("de cuerda", "rasgueos")
    
    def tocar(self):
        print("La guitarra es un instrumento clásico")
        print(f"La guitarra utiliza {self.funcion} y es {self.tipo}")
 
class Piano(Instrumento):
    def __init__(self):
        super().__init__("de teclas", "presión")
    
    def tocar(self):
        print("El piano es un instrumento elegante")
        print(f"El piano utiliza {self.funcion} y es {self.tipo}")
 
class Tambor(Instrumento):
    def __init__(self):
        super().__init__("de percusión", "golpes precisos")
    
    def tocar(self):
        print("El tambor se usa en la samba")
        print(f"El tambor utiliza {self.funcion} y es {self.tipo}")
 
# Uso
guitarra = Guitarra()
piano = Piano()
tambor = Tambor()

guitarra.tocar()
piano.tocar()
tambor.tocar()
