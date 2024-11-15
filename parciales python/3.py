
# Lista de golosinas
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
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

# Diccionario de empleados
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}


clavesTecnico = ("UTN-FRM", "admin", "CCCDDD2020")

golosinasPedidas = []

def pedir_golosina():
    legajo = int(input("Ingrese su legajo: "))
    if legajo in empleados:
        print("Bienvenido, ", empleados[legajo])
        while True:
            codigo = int(input("Ingrese el código de la golosina que desea: "))
            for golosina in golosinas:
                if golosina[0] == codigo:
                    if golosina[2] > 0:
                        golosina[2] -= 1
                        if not any(golosina[1] in pedida for pedida in golosinasPedidas):
                            golosinasPedidas.append([codigo, golosina[1], 1])
                        else:
                            for pedida in golosinasPedidas:
                                if pedida[1] == golosina[1]:
                                    pedida[2] += 1
                        print("Golosina entregada con éxito.")
                        break
                    else:
                        print("Lo sentimos, la golosina no se encuentra disponible.")
                        break
            else:
                print("Código de golosina no válido.")
            respuesta = input("Desea pedir otra golosina? (s/n): ")
            if respuesta.lower() != "s":
                break
    else:
        print("Usted no es un empleado de la empresa.")

def mostrar_golosinas():
    print("Golosinas disponibles:")
    for golosina in golosinas:
        print(f"{golosina[0]} - {golosina[1]} - {golosina[2]}")

def rellenar_golosinas():
    clave1 = input("Ingrese la primera palabra de la clave técnica: ")
    clave2 = input("Ingrese la segunda palabra de la clave técnica: ")
    clave3 = input("Ingrese la tercera palabra de la clave técnica: ")
    if (clave1, clave2, clave3) == clavesTecnico:
        codigo = int(input("Ingrese el código de la golosina a rellenar: "))
        for golosina in golosinas:
            if golosina[0] == codigo:
                cantidad = int(input("Ingrese la cantidad a rellenar: "))
                if cantidad > 0:
                    golosina[2] += cantidad
                    print("Golosina rellenada con éxito.")
                else:
                    print("Cantidad a rellenar no válida.")
                break
        else:
            print("Código de golosina no válido.")
    else:
        print("No tiene permiso para ejecutar la función de recarga.")

def apagar_maquina():
    print("Golosinas pedidas:")
    for pedida in golosinasPedidas:
        print(f"{pedida[0]} - {pedida[1]} - {pedida[2]}")
    total_golosinas = sum(pedida[2] for pedida in golosinasPedidas)
    print(f"Total de golosinas pedidas: {total_golosinas}")

while True:
    print("Menú:")
    print("1. Pedir golosina")
    print("2. Mostrar golosinas")
    print("3. Rellenar golosinas")
    print("4. Apagar máquina")
    opcion = int(input("Ingrese su opción: "))
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
        print("Opción no válida.")
