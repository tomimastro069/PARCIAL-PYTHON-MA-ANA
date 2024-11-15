def crearMatriz(filas, columnas):
    lista = [[0 for _ in range(columnas)] for _ in range(filas)]

    modalidadDeCarga = int(input("Ingrese 1 para cargar la matriz manualmente, 0 para hacerlo con números aleatorios:"))
    while modalidadDeCarga != 1 and modalidadDeCarga != 0:
        modalidadDeCarga = input("Por favor ingrese un valor correcto, 1 para carga manual, 0 para aleatoria:")

    if modalidadDeCarga == 1:
        print("Los valores válidos serán entre 1 y 999. Por favor ingresé valores en ese rango.")
        for i in range(filas):
            for u in range(columnas):
                print("Ingrese el valor numérico de la fila", i+1, "y columna", u+1, ":" )
                while True:
                    try:
                        valor = float(input())
                        lista[i][u] = valor
                        break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número decimal.") # Si ocurre un error de conversión, mostramos un mensaje        
    else:
        import random
        for i in range(filas):
            for u in range(columnas):
                valor = round(random.uniform(1, 999),2)
                lista[i][u] = valor

    return lista

def Main():
    filas = int(input("Ingrese el número de filas de nuestra matríz, debe ser mayor o igual a 3:"))
    while filas < 3:
        filas = int(input("El valor mínimo es 3. Ingrese un valor válido:"))
        
    columnas = int(input("Ingrese el número de columnas de nuestra matríz, debee ser mayor o igual a 2:"))
    while columnas < 2:
        columnas = int(input("El valor mínimo es 2. Ingrese un valor válido:"))

    lista = crearMatriz(filas, columnas)

    for a in range(filas):
                print(lista[a])

if __name__ == "__main__":
    Main()