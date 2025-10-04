class Vino:
    def __init__(self, nombre, tipo, cepa, anio):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio = anio
class Queso:
    def __init__(self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.sal = sal  

#Registrar vinos
vino1 = Vino("Malbec Reserva", "Tinto", "Malbec", 1990)
vino2 = Vino("Chardonnay", "Blanco", "Chardonnay", 1970)
vino3 = Vino("Cabernet Sauvignon", "Tinto", "Cabernet Sauvignon", 2000)
vino4 = Vino("Sauvignon Blanc", "Blanco", "Sauvignon Blanc", 1959)

#Registrar quesos
queso1 = Queso("Cheddar", "Duro", 12,True )
queso2 = Queso("Queso azul", "Maduro", 3, False)
queso3 = Queso("Chaqueño", "Semi-duro", 6, True)

# Mostrar vinos

print("Vinos en inventario:")
print("Vino 1: ", vino1.nombre)     
print(vino1.tipo)
print(vino1.cepa)       
print(vino1.anio)
print("Vino 2: ", vino2.nombre)
print(vino2.tipo)
print(vino2.cepa)
print(vino2.anio)
print("Vino 3: ", vino3.nombre)
print(vino3.tipo)
print(vino3.cepa)
print(vino3.anio)
print("Vino 4: ", vino4.nombre)
print(vino4.tipo)
print(vino4.cepa)
print(vino4.anio)

# Mostrar quesos

print("Quesos en inventario:")
print("Queso 1: ", queso1.nombre)
print(queso1.variedad)
print(queso1.edad)
print(queso1.sal)
print("Queso 2: ", queso2.nombre)
print(queso2.variedad)
print(queso2.edad)
print(queso2.sal)
print("Queso 3:", queso3.nombre)
print(queso3.variedad)
print(queso3.edad)
print(queso3.sal)

 
      
      
      






 



