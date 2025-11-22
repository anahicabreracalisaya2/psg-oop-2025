# Definición
class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            print("El denominador no puede ser cero.")
            return
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otro):
        nuevo_num = self.numerador * otro.denominador + otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)
    def __sub__(self, otro):
        nuevo_num = self.numerador * otro.denominador - otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)
    def __mul__(self, otro):
        nuevo_num = self.numerador * otro.numerador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)
    def __truediv__(self, otro):
        nuevo_num = self.numerador * otro.denominador
        nuevo_den = self.denominador * otro.numerador
        return Fraccion(nuevo_num, nuevo_den)
# Comparaciones
    def __eq__(self, otro):
        return self.numerador * otro.denominador == otro.numerador * self.denominador

    def __lt__(self, otro):
        return self.numerador * otro.denominador < otro.numerador * self.denominador

    def __gt__(self, otro):
        return self.numerador * otro.denominador > otro.numerador * self.denominador

    def __ne__(self, otro):
        return not self == otro

#uso
a = Fraccion(4, 5)
b = Fraccion(7, 8)

print(a)  
print(b)  

print(a + b)  
print(a - b)  
print(a * b)  
print(a / b)  

print(a == b) 
print(a < b)  
print(a > b)  
print(a != b) 
