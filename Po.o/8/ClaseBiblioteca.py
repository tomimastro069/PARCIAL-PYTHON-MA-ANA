
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)


    def buscar_libro(self,titulo):
        encontrado = False
        for i in  self.libros:
           
            if i.titulo == titulo:
                print("\nlibro encontrado\n")
                print(f"Titulo\t   Autor\tAño de publicacion\tGenero\n{i.titulo}\t{i.autor}\t{i.año_publicacion}\t\t{i.genero}")
                encontrado = True
                break
        if not encontrado:
            print("libro no encontrado papi/pedilo")

    def mostrar_todos_los_libros(self):
        for i in self.libros:
            print(f"Titulo\t {i.titulo} \n----------------\nAutor\tAño de publicacion\tGenero\n{i.autor}\t{i.año_publicacion}\t\t\t{i.genero}")
