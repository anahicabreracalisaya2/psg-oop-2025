class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
    def tarea_completada(self):
        self.completada = True