# Descripción
Debes desarrollar un videojuego tipo aventura, donde los personajes tiene distintas habilidades Cada personaje pertenece a uno o más tipos que definen sus comportamientos:
Nadador: Puede ejecutar la acción nadar(), que representa la acción de desplazarse en el agua. Volador: Puede ejecutar la acción volar(), que representa la acción de desplazarse por el aire. En el juego existen tres personajes principales, cada uno con habilidades específicas:
Pez: tiene la habilidad de nadar. Pájaro: tiene la habilidad de volar. Pato: tiene ambas habilidades, puede nadar y volar. Cada personaje debe contar con un método mostrar() que indique el tipo de personaje y su habilidad principal o combinada. Realiza el análisis y diagrama de clases de las clases Nadador, Volador, Pez, Pajaro y Pato

# Requisitos
- Desarrollar un videojuego
- Crear personajes con habilidades específicas.
- Cada personaje puede tener una o más habilidades: nadar y/o volar.
- Las habilidades son nadar o volar.
- Cada personaje muestra su tipo de personaje y sus habilidades.

Objetos:
- Nadador (clase padre)
- Volador (clase padre)
- Pez (clase hija)
- Pajaro (clase hija)
- Pato (clase hija)
Características:
- Nadador:
  - habilidad: String
- Volador:
  - habilidad: String
- Pez
   - (sin características)
- Pajaro
   - (sin características)
- Pato
   - (sin características)
Acciones:
- Nadador:
  - nadar()
- Volador:
  - volar()
- Pez
   - mostrar()
- Pajaro
   - mostrar()
- Pato
   - mostrtar()

```mermaid
classDiagram
    class Nadador {
        +nadar()
    }
    class Volador {
        +volar()
    }
    class Pez {
        +mostrar()
    }
    class Pajaro {
        +mostrar()
    }
    class Pato {
        +mostrar()
    }

    Nadador <|-- Pez
    Volador <|-- Pajaro
    Nadador <|-- Pato
    Volador <|-- Pato
```
