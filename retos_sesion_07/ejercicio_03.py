class Romano:
    _valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100
    }

    def __init__(self, valor: str):
        self._valor_romano = valor.upper()
        self._valor_entero = self._romano_a_entero(self._valor_romano)

    def _romano_a_entero(self, valor: str) -> int:
        total = 0
        i = 0
        valor = valor.upper()

        while i < len(valor):
            actual = self._valores_romanos[valor[i]]

            if i + 1 < len(valor):
                siguiente = self._valores_romanos[valor[i + 1]]

                if actual < siguiente:
                    total += siguiente - actual
                    i += 2
                    continue

            total += actual
            i += 1

        return total

    def _entero_a_romano(self, numero: int) -> str:
        valores = [
            (100, 'C'), (90, 'XC'), (50, 'L'),
            (40, 'XL'), (10, 'X'), (9, 'IX'),
            (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado

    def __add__(self, otro):
        if not isinstance(otro, Romano):
            raise TypeError("Solo se pueden sumar objetos de tipo Romano")
        
        suma = self._valor_entero + otro._valor_entero
        return Romano(self._entero_a_romano(suma))

    def valor_entero(self):
        return self._valor_entero

    def __str__(self):
        return self._valor_romano


# Aplicación
romano1 = Romano("VI")       
romano2 = Romano("III")   
romano3 = romano1 + romano2  
print(f"{romano1} + {romano2} = {romano3} (Valor entero: {romano3.valor_entero()})")
