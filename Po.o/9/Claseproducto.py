class Producto:
    def __init__(self,nombre,categoria,precio,cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    def mostrar_producto(self):
        print(f"PRODUCTO\n------------\nNombre\tCategoria\tPrecio\tCantidad\n{self.nombre}\t{self.categoria}\t{self.precio}\t\t{self.cantidad}")
        
    """Ejercicio 3: Sistema de Inventario de Tienda
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
Mostrar todos los productos en el inventario."""
    