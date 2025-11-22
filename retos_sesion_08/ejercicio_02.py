# Definición
class Destino:
    def __init__(self, nombre, costo):  # Constructor
        self.nombre = nombre
        self.costo = float(costo)

    def __str__(self):  
        return f"[{self.nombre}] ➡ {self.costo} USD"

class Catalogo:
    def __init__(self):  # Constructor
        self.destinos = []  # Lista de destinos

    def __str__(self):
        texto = "🗺 Destinos 🗺\n"
        for i, destino in enumerate(self.destinos, start=1):
            texto += f"{i}. {destino}\n"
        return texto
    def __len__(self):  
        return len(self.destinos)

    def __getitem__(self, indice):  
        return self.destinos[indice]

    def __setitem__(self, indice, valor): 
        self.destinos[indice] = valor

    def __delitem__(self, indice):  
        del self.destinos[indice]

    def __iter__(self):  # Iteración
        return iter(self.destinos)


# Uso
catalogo = Catalogo()
catalogo.destinos.append(Destino("Cochabamba", 1200))
catalogo.destinos.append(Destino("Santa Cruz", 1800))
catalogo.destinos.append(Destino("Mexico", 900))
catalogo.destinos.append(Destino("Lima", 350))
print(catalogo)
print("La cantidad de destinos es:", len(catalogo))
print("Primer destino es:", catalogo[0])
catalogo[1] = Destino("Chile", 1600)
print("\nCatálogo nuevo actualizado:\n", catalogo)
print("\nListado:")
for d in catalogo:
    print(d)
del catalogo[2]
print("\nCatálogo actualizado:")
print(catalogo)
