class Usuario:
  
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libros(self):
        self.libros_prestados.clear()

    def __str__(self):
        return self.nombre