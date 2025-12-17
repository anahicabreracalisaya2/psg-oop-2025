# Análisis
Requisitos:
- Representar un edificio con nombre y dirección.
- El edificio contiene 3 pisos, cada uno identificado por su número.
- Cada piso puede tener:departamento y/o oficianas
- Departamentos: numerados 
- Oficinas: numeradas con el piso seguido de letra
- El edificio tiene direccion y nombre
- los pisos tienen numero
- las oficinas tienen teléfono
- los departamentos tienen inquilino
- Se debe acceder y mostrar informacion del edificio

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
- Edificio:
    - direccion: String
    - nombre: String
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