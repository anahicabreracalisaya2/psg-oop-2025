
- # Análisis
Requisitos:
- Tiene un saldo
- El saldo es privado
- El saldo solo se consulta
- El saldo se cambia modifica a trvéz de depósito y retiro
- Tiene un metodo depositar
- Tienen un metodo retiro cuando el saldo es suficiente
- Tiene número de cuenta privado
  Tiene un método consultar
  Tiene un titular
Objetos:
- Cuenta
Características:
- Cuenta
    - saldo: float
    - numero_cuenta: string
    - nombre_titular: string
Acciones:
- Cuenta:
    - depositar(monto)
    - retirar (monto)
    - get_saldo()
    - get_numero_cuenta()
    - get_nombre_titular()
    - set_nombre_titular(nombre)

	```mermaid
classDiagram
    class Cuenta{
        -saldo: float
        -numero_cuenta: String
        +nombre_titular: String

        +depositar(monto)
        +retirar(monto)
        +get_saldo()
        +get_numero_cuenta()
        +get_nombre_titular()
        +set_nombre_titular(nombre)
    }

```