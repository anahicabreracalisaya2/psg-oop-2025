class Sala:
    __instancia = None
    titulo = ""
    reproducciendo = False
    clientes = []

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def iniciar(self, titulo):
        if self.reproducciendo:
            print("💢 La película ya está en reproducción.")
            return
        self.titulo = titulo
        self.reproducciendo = True
        print(f"🎬 Iniciando la película: {self.titulo}")

    def unirse(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente} se ha unido a la sala.")

    def estado(self):
        estado = "En reproducción" if self.reproducciendo else "Detenida"
        print(f"🎥 Película: {self.titulo} | Estado: {estado}")

    def listar(self):
        print(f"👥 Clientes en la sala: {len(self.clientes)}")
        for cliente in self.clientes:
            print(f"- {cliente}")

    def finalizar(self):
        print("❗ Película finalizada.")
        self.reproducciendo = False

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"👤 {self.nombre}"
    def unirse(self):
        Sala().unirse(self)


while True:
    print("="*30)
    print("🎬 Menú de Cine Virtual")
    print("1. Iniciar película")
    print("2. Unirse a sala")
    print("3. Ver estado")
    print("4. Ver clientes")
    print("5. Finalizar película")
    print("6. Salir")
    print("="*30)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("💬 Título de la película: ")
        Sala().iniciar(titulo)
    elif opcion == "2":
        nombre = input("💬 Tu nombre: ")
        cliente = Cliente(nombre)
        cliente.unirse()
    elif opcion == "3":
        Sala().estado()
    elif opcion == "4":
        Sala().listar()
    elif opcion == "5":
        Sala().finalizar()
    elif opcion == "6":
        break
    else:
        print("💢 Opción no válida.")