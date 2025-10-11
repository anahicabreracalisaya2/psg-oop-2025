class atleta:
    def __init__(self, nombre, energia, fuerza): # Constructor
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza
 
    def entrenar(self,horas): # Método de instancia
        print(f"{self.nombre} entrena por {horas} hrs.")
        self.fuerza += horas
        self.energia -= horas
        print(f"{self.nombre} ha aumentado su fuerza a {self.fuerza} pero su energía es {self.energia}") 

 
    def dormir(self, horas): # Método de instancia
        self.energia += horas
        print(f"{self.nombre} durmió por {horas} hrs.")
        print(f"{self.nombre} ha aumentado su energía a {self.energia + horas}")
       
    def comer(self, comida): # Método de instancia
        if comida == "🍔":
            print(f"El atleta {self.nombre} está comiendo {comida}")
        else:
            print(f"Este atleta no come {comida}")
            
# Instanciando objeto 1
Neil = atleta("Neil",3,2)
Neil.entrenar(2)
Neil.dormir(3)
Neil.comer("🍕")
Neil.comer("🍔")
# Instanciando objeto 2
Ali = atleta("Ali",1,2)
Ali.entrenar(0)
Ali.dormir(1)
Ali.comer("🍿")
Ali.comer("🍔")