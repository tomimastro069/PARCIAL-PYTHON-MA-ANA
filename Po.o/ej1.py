class Celda:
    def __init__(self, fila,columna, valor):
        self.fila = fila
        self.columna = columna 
        self.valor  = valor

class matriz:
    def __init__(self):
        self.celdasMatriz= []
    def agregarcelda(self,  fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and  celda.columna ==columna:
                print(f"la celda en fila |{fila}| y columna:  |{columna}| ya existe")
                return
        nueva_celda = Celda(fila,columna,valor)
        self.celdasMatriz.append(nueva_celda)
    def mostrar_celdas(self):
        for i in self.celdasMatriz:
            print("fila:", i.fila, "Columna:",i.columna,"valor=" ,i.valor)
    def valor_de_celda(self,fila,columna):
        for i in self.celdasMatriz:
            if i.fila == fila and i.columna == columna:
                return i.valor
            else:
                return "la fila y columna no ha sido asignada"
        
        
def main():
    matriz1 = matriz()
    while True:
        valor= input("ingrese el valor para la celda o ingrese |FIN| para terminar la ejecución: ")
        if valor == "FIN":
            break
        fila = int(input("ingrese la fila donde se encuentra la celda: "))
        columna = int(input("ingrese la columna donde se encuentra la celda: "))
        matriz1.agregarcelda(fila, columna, valor)
        matriz1.mostrar_celdas()

if  __name__ == "__main__":
    main()
