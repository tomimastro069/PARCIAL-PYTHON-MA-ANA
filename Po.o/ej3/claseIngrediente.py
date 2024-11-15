class Ingrediente:
    def __init__(self,nombre,cantidad,unidadDeMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadDeMedida = unidadDeMedida
    
    def __str__(self):
        return self.nombre ,self.cantidad, self.unidadDeMedida
        
