##Invertirlistas

cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num

Lista_invertida=[None] * cantidaddefilas




for i in range(len(Lista)):
    Lista_invertida[i]= str(Lista[len(Lista) - 1 - i])



    

print("LISTA ORIGINAL: ")
for i in range(len(Lista)):
    print(Lista[i],end= " | ")
print()
print("----------------------------------")
print("LISTA INVERTIDA: ")
for i in range(len(Lista_invertida)):
    print(Lista_invertida[i],end= " | ")
print()





##MAX/MIN



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




##metodo burbuja




from random import sample 
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


##metodo de insercion


from random import sample 
lista = list(range(100)) 
vectorins = sample(lista,8)

def insertionsort(vectorins): 
    """Esta función ordenara el vector que le pases como argumento con
    el Método Insertion Sort"""
    print("El vector a ordenar con inserción es:", vectorins)
    
    
    
    largo = 0 
     

    for i in vectorins:
        largo += 1 
    
    for i in range(1, largo): 
    
        elemento = vectorins[i] 
        j = i-1
        while j >= 0 and elemento < vectorins[j] : 
                vectorins[j+1] = vectorins[j] 
                j -= 1
        vectorins[j+1] = elemento





        
    print("El vector ordenado con inserción es: ", vectorins)

insertionsort(vectorins)

## TRANSPONER MATRIZ


Matriz = []
transpuesta = [[Matriz[j][i] for j in range(len(Matriz))] for i in range(len(Matriz[0]))]
print("la matriz transpuesta es: ")
for i in transpuesta:
    print(i)
        


## METODO POR SELECCION 



from random import sample

lista = list(range(100)) 
vectorselect = sample(lista,8) 


def selectionsort(vectorselect):
    """Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""
    print ("El vector a ordenar es:",vectorselect)




    largo = 0
    for _ in vectorselect:
        largo += 1 
        
    for i in range(largo): 
        minimo = i
         
        for j in range(i+1, largo): 
            if vectorselect[minimo] > vectorselect[j]: 
                minimo = j 
        vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]
    print("El vector ordenado es: ",vectorselect)




    

selectionsort(vectorselect)