import random
lista = list(range(100)) 
vectorbs = sample(lista,8) 


def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""
    
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
