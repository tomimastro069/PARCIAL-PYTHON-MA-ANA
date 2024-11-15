
golosinas = [
    [1, "KitKat", 20],
    [2, "Chiches", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]


empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "CCCDDD" ,"2020")


golosinasPedidas = []

def pedir_golosina():
    
    legajo = int(input("Ingrese su legajo: "))
    while legajo not in empleados:
        legajo = int(input("Usted no es un empleado de la empresa, una ratata\n"))
    while True:          
        codigo = int(input("Ingrese el codigo de la golosina: "))
        golosina_encontrada = False 

        for i in golosinas:    
            if i[0] == codigo:  
                golosina_encontrada = True
                if i[2] > 0:
                    i[2] -= 1
                    if not any(i[1] in pedida for pedida in golosinasPedidas):
                        golosinasPedidas.append([codigo, i[1], 1])
                    else:
                        for pedida in golosinasPedidas:
                            if pedida[1] == i[1]:
                                pedida[2] += 1
                    print("Golosina pedida")
                else:
                    print("No hay golosinas suficientes")
                break  

        if not golosina_encontrada:
            print("Codigo de golosina inexistente")

        respuesta = input("¿Desea pedir otra golosina? (s/n): ")
        if respuesta.lower() != "s":
            break
            

   
def mostrar_golosinas():
    print("Golosinas disponibles:")
    for golosina in golosinas:
        print(f"{golosina[0]} - {golosina[1]} - {golosina[2]}")

    
def rellenar_golosinas():
    acceso = False
    constraseñaNashe1 = input("Ingrsate la primera contraseña padre\n")
    constraseñaNashe2 = input("Ingresate la second contraseña padre\n")
    constraseñaNashe3 = input("Ingresate la tre contraseña padre\n")
    if constraseñaNashe1 == clavesTecnico[0]:
        print("primera contraseña godeto")
        if constraseñaNashe2 == clavesTecnico[1]:
            print("second contraseña godeto")
            if constraseñaNashe3 == clavesTecnico[2]:
                print("tre contraseña godeto")
                acceso = True
            else: 
                print("sos un petardo anashei")
        else:
            print("Sos alto pete")
    else:
        print("SOS EL TOPO MAYOR")
    if acceso == True:
        encontradonashe = False
        print("hola, como va topo mayoritario?")
        codigo = int(input("Ingrese el codigo de la golosina q desea rellenar\n"))
        for i in golosinas:    
                if i[0] == codigo:
                    cantArellenar= int(input("CUANTO CARAMELO UTE KIERE RELLENA?\n"))
                    i[2]  = i[2] + cantArellenar
                    encontradonashe = True
                    break
        
        if encontradonashe == False:
            print("N O   E S I S T E   E L   C O D I G O ")

def apagar_maquina():
    print("Golosina q ute a pedido:")
    for i in golosinasPedidas:
        print(f"{i[0]} - {i[1]} - {i[2]}")
    total_golosinas = sum(i[2] for i in golosinasPedidas)
    print(f"Total de golosinas pedida por ute: {total_golosinas}")
    
def menu():
    while True:
        print("Menu:")
        print("1. Pedir golosina")
        print("2. Mostrar golosinas")
        print("3. Rellenar golosinas")
        print("4. Apagar máquina")
        opcion = int(input(" "))
        if opcion == 1:
            pedir_golosina()
        elif opcion == 2:
            mostrar_golosinas()
        elif opcion == 3:
            rellenar_golosinas()
        elif opcion == 4:
            apagar_maquina()
            break
        else:
            print("Opcion no valida.")

def main():
    menu()

if __name__ =="__main__":
    main()