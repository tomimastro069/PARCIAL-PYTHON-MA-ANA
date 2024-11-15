
import numpy
import random
def transpuestam(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz


def matrizrotada90grados(matriz):
    matriz = transpuestam(matriz)
    for i in range(0,len(matriz)):
        matriz[i] = numpy.flip(matriz[i])
    return matriz


def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    matriz90 = matrizrotada90grados(Matriz)
    print("La matriz girada 90° hacia la derecha es: ")
    for i in matriz90:
        print(i)
        
if __name__ == "__main__":
    Main()

"""
import random
lista = list(range(100)) 
vectorbs = sample(lista,8) 


def bubblesort(vectorbs):
    print("El vector a ordenar es:",vectorbs)
    n = 0 
    for _ in vectorbs:
        n += 1 
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1] :
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
            
    print ("El vector ordenado es: ",vectorbs)

bubblesort(vectorbs)



## MATRICES


import random

# Definir las dimensiones de la matriz
Columnas = 4
Filas = 3

# Crear una matriz con valores aleatorios entre 0 y 100
Matriz = [[random.randint(0, 100) for _ in range(Columnas)] for _ in range(Filas)]

# Mostrar la matriz original
print("Matriz original:")
for fila in Matriz:
    print(fila)

for i in range(Filas * Columnas - 1):
    for j in range(Filas * Columnas - 1 - i):
            fila1, col1 = j // Columnas, j % Columnas
            fila2, col2 = (j + 1) // Columnas, (j + 1) % Columnas
            
            # Comparar e intercambiar si el elemento está desordenado
            if Matriz[fila1][col1] > Matriz[fila2][col2]:
                Matriz[fila1][col1], Matriz[fila2][col2] = Matriz[fila2][col2], Matriz[fila1][col1]


# Mostrar la matriz ordenada
print("\nMatriz ordenada:")
for fila in Matriz:
    print(fila)

"""



