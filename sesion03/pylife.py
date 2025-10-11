# Definiendo la clase
class Persona:
    def __init__(self, nombre): # Constructor
        self.nombre = nombre
        self.hambre = True # Nuevo
 
    def saludar(self): # Método de instancia
        print(f"Hola, soy {self.nombre}")
 
    def dormir(self, horas): # Método de instancia
        print(f"{self.nombre} duerme por {horas} hrs.")
        print(f"{self.nombre} se ha despertado")
        self.hambre = True # Al despertar tiene hambre
 
    def comer(self, comida): # Nuevo Método de instancia
        if self.hambre:
            print(f"{self.nombre} está comiendo {comida}")
            self.hambre = False
            return "🍽️"
        else:
            print(f"{self.nombre} no tiene hambre")
            return comida
            
# Instanciando un objeto
jhon = Persona("Jhon")
jhon.saludar()
jhon.dormir(8)
# Llamando al método de la instancia
comida = jhon.comer("🍕")
print(f"Devolvió: {comida}")
comida = jhon.comer("🍔")
print(f"Devolvió: {comida}")

# Definiendo la clase
class Perro:
    factor_edad = 7 # Atributo de clase
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad
 
    def ladrar(self): # Método de instancia
        print(f"{self.nombre} dice: ¡Guau!")
 
    def crecer(self, tiempo): # Método de instancia
        self.edad += tiempo
        print(f"{self.nombre} ha crecido {tiempo} años")
 
    @classmethod # Nuevo Método de clase
    def nacer(cls, nombre):
        print(f"{nombre} ha nacido como un cachorro")
        return cls(nombre,0)
 
    @classmethod # Nuevo Método de clase
    def edad_a_humano(cls, perro):
        print(f"En años humanos, {perro.nombre}")
        print(f"tiene {perro.edad * cls.factor_edad} años")
    
# Instanciando un objeto
rex = Perro.nacer("Rex")
rex.ladrar()
rex.crecer(2)
Perro.edad_a_humano(rex)


# Gatito

# Definiendo la clase
class Gato:
    def __init__(self, nombre, color): # Constructor
        self.nombre = nombre
        self.color = color
        self.edad = 0
 
    @classmethod # Método de clase
    def nacer(cls, nombre, color):
        print(f"{nombre} ha nacido como un cachorro")
        return cls(nombre, color)
 
    def crecer(self, tiempo): # Método de instancia
        self.edad += tiempo
        print(f"{self.nombre} ha crecido {tiempo} años")
 
    def maullar(self): # Método de instancia
        print(f"{self.nombre} dice: {Gato.sonidos()[0]}")
 
    @staticmethod # Nuevo Método estático
    def sonidos():
        return ["miau", "ronroneo"]
 
# Instanciando un objeto
mimi = Gato.nacer("Mimi", "blanco")
mimi.maullar()
mimi.crecer(2)
sonidos = Gato.sonidos()
print(f"Sonidos de {mimi.nombre}: {sonidos}")



print("DESDE AQUI")
class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # Método especial
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

jhon = Persona("Jhon", 30)
print(jhon) # Nombre: Jhon, Edad: 30
jane = Persona("Jane", 25)
detalle = str(jane)
print(detalle) # Nombre: Jane, Edad: 25

class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def __repr__(self): # Método especial
        return f"Persona({self.nombre}, {self.edad})"
jhon = Persona("Jhon", 30)
print(repr(jhon)) # Persona(Jhon, 30)
jane = Persona("Jane", 25)
print(repr(jane)) # Persona(Jane, 25)

class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def __del__(self): # Método especial
        print(f"{self.nombre} ha sido eliminado")
jhon = Persona("Jhon", 30)
print(jhon.nombre) # Jhon
del jhon # Jhon ha sido eliminado
jane = Persona("Jane", 25)
print(jane.nombre) # Jane
del jane # Jane ha sido eliminado

class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

jhon = Persona("Jhon", 30)
print(jhon.__dict__) # {'nombre': 'Jhon', 'edad': 30}
jane = Persona("Jane", 25)
print(jane.__dict__) # {'nombre': 'Jane', 'edad': 25}