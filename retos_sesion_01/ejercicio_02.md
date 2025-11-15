Una tienda de ropa quiere ofrecer camisetas y pantalones
Los clientes pueden elegir entre: camiseta
de manga corta o larga y pantalón de mezclilla o tela
Las camisetas pueden ser de color rojo, azul o verde
y los pantalones de color negro, gris o blanco
Las camisetas tienen las tallas: S, M, L, XL
Los pantalones tienen las tallas desde la 32 hasta la 44
# Análisis
Requisitos:
- ofrecer dos tipos de prenda: camisetas y pantalones
- Ofrecer prendas que puedan modificarse segun las opciones
- elegir camisetas de manga corta o larga
- elegir camiseras de color rojo, azul y verde
- elegir camiseras de talla S, M, L y XL
- ofrecer los pantalones de tela: mezclilla o tela
- ofrecer el color del pantalon negro, gris o blanco
- Ofrecer la talla del pantalon de la 32 al 44
- Ver si la prenda esta disponible

Objetos:
- Camiseta
- Pantalon

Características:
- Camiseta
    - manga
    - color
    - talla
Acciones:
 - No hay acciones
- Pantalon
    - material
    - color
    - talla
Acciones:
- No hay acciones
# Diseño:

Clases:
- Camiseta :
    - Nombre: Camiseta
    - Atributos:
          - manga
          - color
          - talla
    - Métodos:
          - (No hay métodos)
- Pantalon :
    - Nombre: Pantalon
    - Atributos:
          - material
          - color
          - talla
    - Métodos:
          - (No hay métodos)



```mermaid
classDiagram
    class Camiseta {
        manga
        color
        talla
    }

    class Pantalon {
        material
        color
        talla
    }
```