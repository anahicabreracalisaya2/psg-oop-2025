class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completa = False
    def completada(self):
        self.completa = True