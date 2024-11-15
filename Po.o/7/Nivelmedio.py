
def nivel_medio(personajes):
    suma = 0
    cont = 0
    for i in personajes:
            suma += i.nivel
            cont += 1
    media = suma / cont
    return media

