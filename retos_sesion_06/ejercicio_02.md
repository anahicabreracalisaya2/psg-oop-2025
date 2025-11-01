# Análisis
Requisitos:
- Representar un edificio con nombre y dirección.
- El edificio contiene 3 pisos, cada uno identificado por su número.
- Cada piso puede tener:
  - Departamentos: numerados con el piso seguido de unidad (ej. 201, 304).
  - Oficinas: numeradas con el piso seguido de letra (ej. 2A, 3C).
- Los departamentos tienen una lista de inquilinos.
- Las oficinas tienen un número de teléfono.
- El sistema debe permitir:
  - Crear el edificio con sus pisos.
  - Agregar departamentos y oficinas a cada piso.
- Mostrar la información del edificio de forma jerárquica




Objetos:
- Piso
- Departamento
- Oficina
- Edificio
Características:
- Piso:
    - numero: int
    - departamentos: List[Departamento]
    - oficinas: List[Oficina]
- Departamento
    - numero: String
    - inquilinos: List[String]
- Oficina
    - numero: string
    - telefono: int
- Cuerpo:
    - nombre: String
    - corazón: Corazón
Acciones:
- Piso:
    - agregar_departamento(departamento:departamento)
    - agregar_oficina(oficina:oficina)
- Departamento:
    - mostrar()
- Oficina
    - mostrar()
  


```mermaid
classDiagram
    class Edificio {
        +nombre: String
        +direccion: String
        +pisos: List[Piso]
        +mostrar_info()
    }

    class Piso {
        +numero: int
        +departamentos: List[Departamento]
        +oficinas: List[Oficina]
        +agregar_departamento(depto: Departamento)
        +agregar_oficina(oficina: Oficina)
        +mostrar_info()
    }

    class Departamento {
        +numero: String
        +inquilinos: List[String]
        +mostrar_info()
    }

    class Oficina {
        +numero: String
        +telefono: String
        +mostrar_info()
    }

    Edificio o-- Piso
    Piso o-- Departamento
    Piso o-- Oficina
```