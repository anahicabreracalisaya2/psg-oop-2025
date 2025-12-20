from modelos.libro import Libro
from modelos.usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []


    def agregar_libro(self, titulo, autor, isbn):        
        self.libros.append(Libro(titulo, autor, isbn))


    def mostrar_libros(self):       
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for indice, libro in enumerate(self.libros, 1):
                print(f"{indice}. {libro}")


    def registrar_usuario(self, nombre):        
        usuario = next((u for u in self.usuarios if u.nombre == nombre), None)
        if not usuario:
            usuario = Usuario(nombre)
            self.usuarios.append(usuario)
        return usuario


    def prestar_libro(self, usuario, indice):        
        if 0 < indice <= len(self.libros):
            libro = self.libros[indice - 1]
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Índice de libro inválido.")



    def devolver_libros(self, usuario):        
        if usuario.libros_prestados:
            usuario.devolver_libros()
            print(f"{usuario.nombre} devolvió todos sus libros.")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


    def mostrar_prestamos(self):       
        if not any(u.libros_prestados for u in self.usuarios):
            print("No hay préstamos registrados.")
        else:
            for usuario in self.usuarios:
                if usuario.libros_prestados:
                    print(f"{usuario.nombre} tiene prestados:")
                    for libro in usuario.libros_prestados:
                        print(f"   - {libro}")