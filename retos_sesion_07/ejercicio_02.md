# Análisis
Requisitos
- Permitir a los usuarios practicar con distintos instrumentos
- La guitarra emite el sonido strum
- El piano emite el sonido plin
- El tambor emite el sonido boom


Objetos
- Instrumento
    - Guitarra
    - Piano
    - Tambor

Características
- Instrumento: material,nombre
- Guitarra: numero_cuerdas
- Piano: numero_teclas
- Tambor: Tipo_percusion

Acciones
- Guitarra:tocar
- Piano: tocar
- Tambor tocar
- Instrumento:  tocar

```mermaid
classDiagram
class Instrumento {
-nombre: String
-material: String
+tocar()
}


class Guitarra {
-numero_cuerdas: int
+tocar()
}


class Piano {
-numero_teclas: int
+tocar()
}


class Tambor {
-tipo_percusion: String
+tocar()
}


Instrumento <|-- Guitarra
Instrumento <|-- Piano
Instrumento <|-- Tambor
```