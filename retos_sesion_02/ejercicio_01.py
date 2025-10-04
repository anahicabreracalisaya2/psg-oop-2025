class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo=tipo
        self.lugar=lugar
 

Llama = Animal("Llama andina","Mamífero","Altiplano")
Mono = Animal("Capuchino","Mamífero","Selva")
Cocodrilo = Animal("Cocodrilo Americano","Reptil","Amazonas")
Aguila = Animal("Aguila calva","Ave","Los Andes")

 
print("Animales del zoológico registrados:")
print("Animal 1: ", Llama.especie)
print(Llama.origen)
print(Llama.tipo)
print(Llama.lugar)

print("Animal 2: ", Mono.especie)
print(Mono.origen)
print(Mono.tipo)
print(Mono.lugar)

print("Animal 3: ", Cocodrilo.especie)
print(Cocodrilo.origen)
print(Cocodrilo.tipo)
print(Cocodrilo.lugar)

print("Animal 4: ", Aguila.especie)
print(Aguila.origen)
print(Aguila.tipo)
print(Aguila.lugar)



