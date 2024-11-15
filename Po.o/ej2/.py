class Libro:
    def __init__(self, titulo, autor, año_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero

    def mostrar_info(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.año_publicacion}\nGénero: {self.genero}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro.mostrar_info()
        return "Libro no encontrado"

    def mostrar_todos_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca"
        info_libros = ""
        for libro in self.libros:
            info_libros += libro.mostrar_info() + "\n\n"
        return info_libros

class GestorBiblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def ejecutar(self):
        while True:
            print("1. Agregar libro")
            print("2. Buscar libro")
            print("3. Mostrar todos los libros")
            print("4. Salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                año_publicacion = int(input("Ingrese el año de publicación del libro: "))
                genero = input("Ingrese el género del libro: ")
                libro = Libro(titulo, autor, año_publicacion, genero)
                self.biblioteca.agregar_libro(libro)
            elif opcion == "2":
                titulo = input("Ingrese el título del libro a buscar: ")
                print(self.biblioteca.buscar_libro(titulo))
            elif opcion == "3":
                print(self.biblioteca.mostrar_todos_libros())
            elif opcion == "4":
                break
            else:
                print("Opción inválida")

gestor = GestorBiblioteca()
gestor.ejecutar()