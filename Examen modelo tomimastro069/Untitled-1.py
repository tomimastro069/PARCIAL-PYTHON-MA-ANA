import random

def LlenarMatriz(Filas, Columnas):
    matriz = [[0] * Columnas for _ in range(Filas)]
    for i in range(Filas):
        for j in range(Columnas):
            valor = float(input(f"ingrese el valor de la casilla {i} {j}: "))
            while valor > 999 or valor < 0:
                valor = float(input("Por favor ingrese un numero en el rango de 0 a 999: "))
            matriz [i] [j] = valor
    return matriz

def LlenarMatrizAleatoria(Filas,Columnas):
    matriz = [[0]*Columnas for _ in range(Filas)]
    for i in range(Filas):
        for j in range(Columnas):
            valor = random.randint(0,999)
            matriz [i][j] = valor
    return matriz


def Consulta_de_valor(Filas, Columnas):
    Eleccion = int(input("Como quiere llenar la matriz? \n 1 | Manualmente \n 2 | Aleatoriamente \n"))
    match Eleccion:
        case 1: return LlenarMatriz(Filas, Columnas)
        
        case 2: return LlenarMatrizAleatoria(Filas, Columnas)

        case _: 
            print("Opcion invalida, ingrese 1 o 2")
            Consulta_de_valor(Filas, Columnas) 


def Sumar_filas(Matriz):
    Sumarfilas =[0] * len(Matriz)

    for i in range(len(Matriz)):
        suma_valor_fila = 0
        for j in Matriz[i]:
            suma_valor_fila = suma_valor_fila + j
        Sumarfilas[i] = suma_valor_fila

    print("Las sumas de las filas de la matriz son: \n")

    for i in range(len(Sumarfilas)):
        print(f"La suma de la fila {i} es: {Sumarfilas[i]}")

    return Sumarfilas


def Ordenar_mayor_menor_y_orden_original(sumadefilas):
    lista_tuplas = [(sumadefilas[i], i) for i in range(len(sumadefilas))]
    
    n = len(lista_tuplas)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_tuplas[j][0] > lista_tuplas[j+1][0] :
                lista_tuplas[j], lista_tuplas[j+1] = lista_tuplas[j+1], lista_tuplas[j]
    
    print("La lista ordenada de mayor a menor con su orden original es: ")
    for i in lista_tuplas:
        print(i)
    return lista_tuplas


def suma_de_todas_las_filas(sumadefilas):
    sumafinal = 0
    for i in range(len(sumadefilas)):
        sumafinal = sumafinal + sumadefilas [i] 
    print(f"la suma de todas las filas es: {sumafinal}")


def Main():
    
    Filas = int(input("Ingrese la cantidad de filas: (mayor a 3) "))
    
    while Filas < 3:   
        Filas = int(input("Ingrese un numero mayor a 3: "))
    Columnas = int(input("Ingrese la cantidad de filas: (mayor a 2) "))
    
    while Columnas < 2:
        Columnas = int(input("Ingrese un numeroe mayor a 2: "))
    Matriz = Consulta_de_valor(Filas, Columnas)
    
    for i in Matriz:
        print(i)
    print("\n")

    sumadefilas= Sumar_filas(Matriz)
    
    mayor_menor = Ordenar_mayor_menor_y_orden_original(sumadefilas)
    
    sumatotal = suma_de_todas_las_filas(sumadefilas)

if __name__== "__main__":
    Main()