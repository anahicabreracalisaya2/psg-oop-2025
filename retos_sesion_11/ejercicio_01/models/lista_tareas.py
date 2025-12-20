from .tarea import Tarea
class ListaTareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion):
        self.tareas.append(Tarea(descripcion))
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                estado = "✔️" if tarea.completada else " "
                print(f"{i}. [{estado}] {tarea.descripcion} ")
    def completar_tarea(self, i):
        if 0 < i <= len(self.tareas):
            self.tareas[i-1].completada = True
            print(f"Tarea '{self.tareas[i-1].descripcion}' marcada como completada.")
        else:
            print("Índice de tarea inválido.")
    def eliminar_tarea(self, i):
        if 0 < i <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(i-1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        else:
            print("Índice de tarea inválido.")
    def eliminar_completadas(self):
        self.tareas = [tarea for tarea in self.tareas if not tarea.completada]
        print("Tareas completadas eliminadas.")
    def eliminar_todas(self):
        self.tareas.clear()
        print("Todas las tareas eliminadas.")