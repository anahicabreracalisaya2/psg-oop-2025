from logica.biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("La cenicienta", "Miguel de Orozco", "CCL-567")
    biblioteca.agregar_libro("La chascañahui", "Antonio Dias Villamil", "HJI-987")
    biblioteca.agregar_libro("Rayuela", "Mario Vargas Llosa", "ASD-565")

    while True:
        print("\n--- Biblioteca Municipal ---")
        print("1. Registrar usuario")
        print("2. Ver libros disponibles")
        print("3. Prestar libro")
        print("4. Devolver libros")
        print("5. Ver préstamos")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = biblioteca.registrar_usuario(nombre)
            print(f"Usuario '{usuario.nombre}' registrado.")
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = biblioteca.registrar_usuario(nombre)
            biblioteca.mostrar_libros()
            indice = int(input("Ingrese el índice del libro a prestar: "))
            biblioteca.prestar_libro(usuario, indice)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = biblioteca.registrar_usuario(nombre)
            biblioteca.devolver_libros(usuario)
        elif opcion == "5":
            biblioteca.mostrar_prestamos()
        elif opcion == "6" or opcion.lower() == "salir":
            print("¡Gracias por usar la Biblioteca Municipal! 📚")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()