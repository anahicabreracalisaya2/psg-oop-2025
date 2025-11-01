class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos  

    def mostrar_info(self):
        print(f"🏠 Departamento {self.numero}")
        print("Inquilinos:")
        for nombre in self.inquilinos:
            print(f" - {nombre}")


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def mostrar_info(self):
        print(f"💼 Oficina {self.numero}")
        print(f"Teléfono: {self.telefono}")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)
 
    def mostrar_info(self):
        print(f"\n Piso {self.numero}")
        for depto in self.departamentos:
            depto.mostrar_info()
        for oficina in self.oficinas:
            oficina.mostrar_info()


class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def agregar_piso(self, piso):
        self.pisos.append(piso)

    def mostrar_info(self):
        print(f"🏣 Edificio: {self.nombre}")
        print(f"📍 Dirección: {self.direccion}")
        for piso in self.pisos:
            piso.mostrar_info()

# Implementacion
edificio = Edificio("Torre Rubi", "Av. Tembladerani #1536")
piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)
print("Agregando departamentos y oficinas...")
piso1.agregar_departamento(Departamento("101", ["Carlita", "Rafael","Camila"]))
piso1.agregar_oficina(Oficina("1B", 7123456))
piso2.agregar_departamento(Departamento("207", ["Eduarda", "Abel"]))
piso3.agregar_departamento(Departamento("309", ["Maruja"]))
piso2.agregar_oficina(Oficina("2A", 7720565))
piso3.agregar_oficina(Oficina("3C", 6783452))
print("\nAgregando pisos al edificio...")
edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)
print("\nInformación del Edificio:")
edificio.mostrar_info()