
class inventario:
    def __init__(self):
        self.listaobjproducto = []
    def agregar_producto(self,producto):
        self.listaobjproducto.append(producto)

    def buscar_producto(self,nombre):
        for i in self.listaobjproducto:
            if i.nombre == nombre:
                print("Articulo encontrado\n ------------------\n")
                i.mostrar_producto()
                return
            else:
                print("Articulo no encontrado")
    def mostrar_todo_el_inventario(self):
        for i in self.listaobjproducto:
            print(i.mostrar_producto())

    """
    Ejercicio 3: Sistema de Inventario de Tienda
Clases a implementar:

Producto

Atributos: nombre (cadena), categoria (cadena), precio (decimal), cantidad (entero).
Métodos:
mostrar_producto(): muestra la información del producto.
Inventario

Atributos: lista de objetos productos[].
Métodos:
agregar_producto(producto): agrega un producto al inventario.
buscar_producto(nombre): busca un producto por su nombre y devuelve la información o un mensaje si no se encuentra.
mostrar_inventario(): muestra todos los productos y su cantidad en el inventario.
GestorInventario (clase con el método main para ejecutar el código)

El programa debe permitir al usuario:
Agregar productos al inventario.
Buscar un producto específico por nombre.
Mostrar todos los productos en el inventario.
    """