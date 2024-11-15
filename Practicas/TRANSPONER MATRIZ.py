 

Matriz = []
transpuesta = [[Matriz[j][i] for j in range(len(Matriz))] for i in range(len(Matriz[0]))]
print("la matriz transpuesta es: ")
for i in transpuesta:
    print(i)


Columnas = 3
Filas = 2

matriz = [[0]*Columnas for _ in range(Filas)]
for i in range(Filas):
    for j in range(Columnas):
       matriz [i][j] = input()

for i in matriz:
    print(i)



   