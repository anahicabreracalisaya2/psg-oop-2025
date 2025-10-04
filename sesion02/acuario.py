class Pez:
    origen = "criado en cautiverio"
    def __init__(self, especie, peso, agua):
        self.especie = especie
        self.peso = peso
        self.agua = agua

print ("Peces encontrados...🐠")
pez1 = Pez("Pez payaso", 0.5, "agua dulce")
pez2 = Pez("Pez betta", 0.3, "agua dulce")
print("Pez 1: ",pez1.origen, pez1.especie, pez1.peso, pez1.agua)
print("Pez 2: ",pez2.origen, pez2.especie, pez2.peso, pez2.agua)

print("Liberando peces...")
pez1.peso = 0.6
pez2.peso = 0.4
Pez.origen = "liberado"

print("Peces liberados...🐟")
print("Pez 1: ",pez1.origen, pez1.especie, pez1.peso, pez1.agua)
print("Pez 2: ",pez2.origen, pez2.especie, pez2.peso, pez2.agua)