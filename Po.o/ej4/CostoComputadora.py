from computadora import Computadora
from compenente import Componentecpu
def mostrar(computadora):
    print(f"Computadora \n-------------\nMarca: \t Modelo\n{computadora.marca} \t {computadora.modelo} \n")
    costototal = 0
    for  componente in computadora.listadeobjetosComponenteCPU:
        costototal += componente.precio * componente.cantidad
        print(f"Componente\tMarca\tCantidad\tPrecio\n{componente.componente}\t\t{componente.marca}\t{componente.cantidad}\t\t{componente.precio}")
    if costototal < 50000:
        precio_venta = costototal * 1.40  
    else:
        precio_venta = costototal * 1.30
    print(f"\n Costo Total \t Precio de venta sugerido\n {costototal}\t\t {precio_venta}")

def main():
    computadoras = []
    while True:  
        marca = input("Ingrese la marca de la computadora: ")
        modelo = input("Ingrese el modelo de la computadora: ")
        computadora1 = Computadora(marca, modelo)
        
        while True:
            componente_nombre = input("Ingrese el componente: ")
            componente_marca = input("Ingrese la marca: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            
            componente1 = Componentecpu(componente_nombre, componente_marca, cantidad, precio)
            computadora1.agregar_componente(componente1)
            
            continuarcomp = input("¿Desea agregar otro componente? (s/n): ")
            if continuarcomp.lower() == "n":
                break

        computadoras.append(computadora1)

        if input("¿Desea cotizar una nueva computadora? (s/n): ").lower() == "n":
            break
    for computadora in computadoras:
        mostrar(computadora)




if __name__ == "__main__":
    main()




