from ClaseBiblioteca import Biblioteca
from Claselibro import libro
class gestor_biblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()
    def agregar_libro1(self):
        
        while True:
            titulo  = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            añop = input("Ingrese el año de publicacion (formato: AAAA): ")
            genero = input("Ingrese el genero del libro: (no trans ni gei) \n")
            libro1 = libro(titulo, autor, añop, genero)
            self.biblioteca.agregar_libro(libro1) 
            continuar = input("Desea continuar? (s/n)\n")
            if continuar.lower() == "n":
                break
    def buscar_libro(self):
        
        while True:
            titulo = input("Ingrese el titulo del libro que desea buscar: ")
            self.biblioteca.buscar_libro(titulo)
            continuar = input("desea buscar otro libro?  (s/n)\n")

            if continuar .lower() == "n":
                break
    def mostrartodo(self):
        self.biblioteca.mostrar_todos_los_libros()
def main():
    menu =gestor_biblioteca()
    menu.agregar_libro1()
    menu.buscar_libro()
    menu.mostrartodo()

    
if __name__== "__main__":
    main()