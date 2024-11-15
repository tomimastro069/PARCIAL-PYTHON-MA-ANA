def obtener_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

def obtener_minimo(lista):
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

lista = [3, 7, 1, 9, 2]
maximo = obtener_maximo(lista)
minimo = obtener_minimo(lista)

print("Máximo:", maximo)
print("Mínimo:", minimo)
