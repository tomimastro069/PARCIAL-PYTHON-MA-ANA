
class Barrio:

    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.ListaDeObjetosVivienda = []


    def agregar_vivienda(self,vivienda):
        self.ListaDeObjetosVivienda.append(vivienda)


    def getSuperficieTotalTerreno(self):
        totaldemetrosdeterreno = 0
        for vivienda in self.ListaDeObjetosVivienda:
            totaldemetrosdeterreno  += vivienda.superficieTerreno
        return totaldemetrosdeterreno
    

    def getSuperficieTotalTerrenoXManzana(self,manzana):
        totaldemetrosdeterrenoxmanzana = 0
        for vivienda in self.ListaDeObjetosVivienda:
            if  vivienda.manzana == manzana:
                totaldemetrosdeterrenoxmanzana += vivienda.superficieTerreno
            return totaldemetrosdeterrenoxmanzana
        

    def getSuperficieTotalCubierta(self):
        totaldemetrosdecubierta = 0
        for vivienda in self.ListaDeObjetosVivienda:
            totaldemetrosdecubierta += vivienda.getMetrosCuadradosCubiertos()
        return  totaldemetrosdecubierta

