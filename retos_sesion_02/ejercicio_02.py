class Vino:
    def __init__(self, nombre, tipo, cepa, anio_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio_produccion = anio_produccion
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
print("Vino 1: ", vino1.nombre,vino1.tipo, vino1.cepa, vino1.anio_produccion)     
print("Vino 2: ", vino2.nombre, vino2.tipo, vino2.cepa, vino2.anio_produccion)
print("Vino 3: ", vino3.nombre, vino3.tipo, vino3.cepa, vino3.anio_produccion)
print("Vino 4: ", vino4.nombre, vino4.tipo, vino4.cepa, vino4.anio_produccion)
print("Quesos en inventario:")
print("Queso 1: ", queso1.nombre,queso1.variedad, queso1.edad, queso1.sal)
print("Queso 2: ", queso2.nombre, queso2.variedad, queso2.edad, queso2.sal)
print("Queso 3:", queso3.nombre, queso3.variedad, queso3.edad, queso3.sal)

 
      
      
      






 



