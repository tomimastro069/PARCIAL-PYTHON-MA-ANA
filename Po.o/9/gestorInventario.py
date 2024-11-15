from ClaseInventario import inventario
from Claseproducto import Producto

class GestorInventario:
    def __init__(self):
        self.inventario = inventario()
    def menu(self):
        while True:
            print("1. Agregar producto")
            print("2. Buscar producto")
            print("3. Mostrar inventario")
            print("4. Salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoría del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto1 = Producto(nombre, categoria, precio, cantidad)
                self.inventario.agregar_producto(producto1)
            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                self.inventario.buscar_producto(nombre)
            elif opcion == "3":
                self.inventario.mostrar_todo_el_inventario()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")
def main():
      menu = GestorInventario()
      menu.menu()
if __name__ =="__main__":
    main()
    
  