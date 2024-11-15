
def encontrar_repetidos(Lista):
    frecuencia={}
    for i in Lista:
        if i in frecuencia:
            frecuencia[i] = frecuencia[i] + 1
        else:
            frecuencia[i] = 1
    repetidos = [i for i, count in frecuencia.items() if count > 1]
    return repetidos

def mayor_menor_y_orden_original(sumadefilas):
    lista_tuplas = [(sumadefilas[i], i) for i in range(len(sumadefilas))]
    n = len(lista_tuplas)
    for i in range(n):
        for j in range(0, n-i-1): #forma de optimizacion del codigo, mientras itera va ordenando y no reordena lo q ya antes se ordenó
            if lista_tuplas[j][0] < lista_tuplas[j+1][0]: 
                lista_tuplas[j], lista_tuplas[j+1] = lista_tuplas[j+1], lista_tuplas[j]
    print("La Lista ordenada de mayor a menor con su orden original a la derecha es: ")
    for i in lista_tuplas:
        print(i)
    return lista_tuplas

def main():
    cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
    Lista = [None] * cantidaddefilas
    for i in range(len(Lista)):
        Num = int(input(f"Ingrese el número de la casilla {i}: "))
        Lista[i] = Num

    elementos_repetidos = encontrar_repetidos(Lista)
    if elementos_repetidos:
        print("Los elementos que se repiten en la lista son:", elementos_repetidos)
    else:
        print("No hay elementos repetidos en la lista.")
    mayorymenor = mayor_menor_y_orden_original(Lista)
if __name__ == "__main__":
    main()

