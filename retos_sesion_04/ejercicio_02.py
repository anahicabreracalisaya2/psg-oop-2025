class Celula:
    def __init__(self, adn_cel, tipo_celula):
        self.adn = adn_cel
        self.__energia = 100
        self.tipo_celula = tipo_celula

    def comer(self):
        print(f"🍽️ La célula ha comido. Energía actual: {self.__energia}")
        self.__energia += 25
    def dividirse(self):
        costo_division = 20
        if self.__energia >= costo_division:
            self.__energia -= costo_division
            print(f"🧬 La célula se ha dividido. Energía restante: {self.__energia}")
        else:
            print("❌ Energía insuficiente para dividirse.")

    def adn(self):
        print(f"🧬 ADN de la célula: {self.adn}")
        return self.adn
    
    def tipo_celula(self):
        print(f"🧫 Tipo de célula: {self.tipo_celula}")
        return self.tipo_celula

    def modifica_tipo(self, nuevo_tipo):
        if self.tipo_celula != nuevo_tipo:
            self.tipo_celula = nuevo_tipo
            print(f"🧫 Tipo de célula modificado a: {self.tipo_celula}")
        else:
            print("⚠️ Tipo de célula inválido. No se realizaron cambios.")

    def energia(self):
        print(f"⚡ Energía actual de la célula: {self.__energia}")
        return self.__energia
    
# Implementando la clase
 
celu=Celula("ABC123", "somática")
print("Se creo una selula con las siguientes caracteristicas: ")
print("ADN:", celu.adn)
print("Tipo:", celu.tipo_celula)
celu.dividirse()
print("Energía después de dividirse:", celu.energia())
celu.comer()
print("Energía después de comer:", celu.energia())
print("Modificando tipo de célula a 'muscular'...")
celu.modifica_tipo("muscular")
print("Nuevo tipo de célula:", celu.tipo_celula)
