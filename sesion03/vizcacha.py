# Definiendo la clase
class Vizcacha:
    def __init__(self): # Constructor
        self.escondido = False
        self.estado = "feliz"
 
    def comer(self, comida): # Método de instancia
        if comida == "🥕":
            print(f"Vizcacha está comiendo {comida}")
        else:
            print(f"Vizcacha no come {comida}")
 
    def excavar(self): # Método de instancia
        print("Vizcacha está excavando un agujero")
        self.escondido = True
        self.estado = "asustada"
        print(f"Vizcacha esta {self.estado}")
 
    def silvar(self): # Método de instancia
        print("iiih iiih")
        self.estado = "feliz"
        print(f"Vizcacha esta {self.estado}")
 
# Instanciando un objeto
vizcacha = Vizcacha()
vizcacha.comer("🥕")
vizcacha.comer("🍔")
vizcacha.excavar()
vizcacha.silvar()