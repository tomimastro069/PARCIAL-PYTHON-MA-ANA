class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto.mostrar_producto()
        return "Producto no encontrado"

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto.mostrar_producto())

class GestorInventario:
    def __init__(self):
        self.inventario = Inventario()

    def ejecutar(self):
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
                producto = Producto(nombre, categoria, precio, cantidad)
                self.inventario.agregar_producto(producto)
            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                print(self.inventario.buscar_producto(nombre))
            elif opcion == "3":
                self.inventario.mostrar_inventario()
            elif opcion == "4":
                break
            else:
                print("Opción inválida")

gestor = GestorInventario()
gestor.ejecutar()