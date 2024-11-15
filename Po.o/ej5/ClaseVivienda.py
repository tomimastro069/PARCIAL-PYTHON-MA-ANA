from ClaseHabitacion import Habitacion
class Vivienda:
    def __init__(self, calle, numero, manzana,nrocasa,superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nrocasa = nrocasa
        self.superficieTerreno = superficieTerreno
        self.ListaObjHabitacion = []
    def agregar_habitacion(self,habitacion):
        self.ListaObjHabitacion.append(habitacion)
        
    def getMetrosCuadradosCubiertos(self):
        total_cubiertos = 0
        for habitacion in  self.ListaObjHabitacion:
            total_cubiertos += habitacion.metrosCuadrados 
        if  total_cubiertos > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total_cubiertos



