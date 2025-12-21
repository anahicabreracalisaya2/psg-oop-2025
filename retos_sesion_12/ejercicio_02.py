class Tarea:
    """
    Representa una tarea individual dentro del sistema.
    """

    def __init__(self, titulo: str, descripcion: str) -> None:
        """
        Inicializa una nueva tarea.

        Parameters
        ----------
        titulo : str
            Título de la tarea.
        descripcion : str
            Descripción de la tarea.
        """
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.completada: bool = False

    def marcar_completada(self) -> None:
        """
        Marca la tarea como completada.
        """
        self.completada = True


class GestorDeTareas:
    """
    Gestiona una colección de tareas.

    Permite agregar, eliminar, marcar como completadas
    y listar tareas.
    """

    def __init__(self) -> None:
        """
        Inicializa el gestor con una lista vacía de tareas.
        """
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, titulo: str, descripcion: str) -> None:
        """
        Agrega una nueva tarea al gestor.

        Parameters
        ----------
        titulo : str
            Título de la tarea.
        descripcion : str
            Descripción de la tarea.
        """
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print(f"✅ Tarea '{titulo}' agregada correctamente.")

    def eliminar_tarea(self, titulo: str) -> None:
        """
        Elimina una tarea según su título.

        Parameters
        ----------
        titulo : str
            Título de la tarea a eliminar.
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"🗑️ Tarea '{titulo}' eliminada.")
                return

        print(f"⚠️ No se encontró la tarea '{titulo}'.")

    def marcar_tarea_completada(self, titulo: str) -> None:
        """
        Marca una tarea como completada según su título.

        Parameters
        ----------
        titulo : str
            Título de la tarea a marcar como completada.
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.marcar_completada()
                print(f"✔️ Tarea '{titulo}' marcada como completada.")
                return

        print(f"⚠️ No se encontró la tarea '{titulo}'.")

    def listar_tareas(self) -> None:
        """
        Muestra todas las tareas con su estado actual.
        """
        if not self.tareas:
            print("📭 No hay tareas registradas.")
            return

        print("\n📋 Lista de tareas:")
        for tarea in self.tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"- {tarea.titulo}: {estado}")


def mostrar_menu() -> None:
    """
    Muestra el menú de opciones del sistema.
    """
    print("\n📌 MENÚ DE TAREAS")
    print("1. Agregar nueva tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar tareas")
    print("5. Salir")


gestor = GestorDeTareas()
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        titulo = input("Ingrese el título de la tarea: ").strip()
        descripcion = input("Ingrese la descripción de la tarea: ").strip()
        gestor.agregar_tarea(titulo, descripcion)
    elif opcion == "2":
        titulo = input("Ingrese el título de la tarea a eliminar: ").strip()
        gestor.eliminar_tarea(titulo)
    elif opcion == "3":
        titulo = input("Ingrese el título de la tarea a completar: ").strip()
        gestor.marcar_tarea_completada(titulo)
    elif opcion == "4":
        gestor.listar_tareas()
    elif opcion == "5":
        print("👋 Saliendo del gestor de tareas. ¡Hasta luego!")
        break
    else:
        print("❌ Opción inválida. Intente nuevamente.")


