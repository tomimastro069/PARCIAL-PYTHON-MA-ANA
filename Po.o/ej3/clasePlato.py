class Plato:
    def __init__(self,Nombre_completo,precio,Esbebida,listaDeIngredientes: list = []):
        self.Nombre_completo = Nombre_completo
        self.precio = precio
        self.Esbebida = Esbebida
        self.listaDeIngredientes = []


    def agregar_ingrediente(self, ingrediente):
        self.listaDeIngredientes.append(ingrediente)
        
    def __str__(self):
        return self.Nombre_completo, self.precio, self.Esbebida, self.listaDeIngredientes
