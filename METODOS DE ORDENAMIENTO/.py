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
