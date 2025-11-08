# Análisis
Requisitos
- Crear una calculadora de numeros romanos
- Los numeros romanos se almacenan como cadena
- Se debe convertir numeros a romanos
- El resultado debe ser en numeros romanos

Objetos
valor

Característica
valor: romano, decimal
Acciones

```mermaid
classDiagram
class Romano {
    -valor_romano: String
    -valor_decimal: int
    +sumar (Romano)
    -romano_a_decimal(valor_romano) 
    -decimal_a_romano(valor_decimal) 
    +mostrar()
}
```