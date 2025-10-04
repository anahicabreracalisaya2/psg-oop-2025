class Perro:
    especie = "canino"
    tipo = "mamífero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.propietario = propietario
toby = Perro("Toby", 3, "macho", "labrador", "Juan")
luna = Perro("Luna", 2, "hembra", "pug", "Jane")
print("Toby: ",toby.tipo, toby.especie, toby.habitat)
print(toby.nombre)
print(toby.edad)
print(toby.genero)
print(toby.raza)
print(toby.propietario)
print("Luna: ",luna.tipo, luna.especie, luna.habitat)
print(luna.nombre)
print(luna.edad)
print(luna.genero)
print(luna.raza)
print(luna.propietario)
print("Perro es: ", Perro.tipo, "Especie: ", Perro.especie, "Habitat: ", Perro.habitat)