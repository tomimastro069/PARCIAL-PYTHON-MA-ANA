from clasePlato import Plato
from claseIngrediente import  Ingrediente

class MenuRestaurant:

    def __init__(self):
        self.platos = []

    def agregar_plato(self):
        j = 1
        while True:

            nombre = input(f"Ingrese el nombre del plato {j}:\n")
           
            precio = float(input("ingrese el precio del plato:\n"))
            while  precio < 0:
                precio = float(input("ingrese el precio del plato (mayor a 0):\n"))

            es_bebida = input("Es bebida? (s/n)")
            es_bebida = es_bebida.lower()
            while es_bebida  not in ["s", "n"]:
                es_bebida = input("Es bebida? (s/n)")

            if es_bebida == "n":
                es_bebida = False
            else:
                es_bebida = True

            plato = Plato(nombre, precio, es_bebida)

            if not es_bebida:
                i = 1
                while True:

                    IngredienteNombre= input(f"ingrese el ingrediente {i} del plato:\n")
                    cantidad = float(input("Ingrese la cantidad de ingredientes:\n"))
                    unidad_medida = input("Ingrese la unidad de medida: \n")
                    ingrediente = Ingrediente(IngredienteNombre,cantidad, unidad_medida)
                    plato.agregar_ingrediente(ingrediente)
                    continuar = input("Desea ingresar otro ingrediente? (s/n)")
                    continuar = continuar.lower()

                    while continuar  not in ["s", "n"]:
                        continuar = input("Desea ingresar otro ingrediente? (s/n)")
                    i  += 1

                    if continuar == "n":
                        break

            self.platos.append(plato)
            continuar = input("Desea agregar otro plato? (s/n) \n")

            if continuar == "n":
                break
            j += 1

    def mostrar_menu(self):

        if not self.platos:
            print("No hay platos en el menú")

        else:
            print("|| Menú del restaurante || \n")

            for plato in self.platos:
                if plato.Esbebida:
                    print(f"Bebida: {plato.Nombre_completo} \n Precio: {plato.precio}\n")
                else:
                    print(f"Plato: {plato.Nombre_completo} \n------- \n Precio: {plato.precio} \n ------------\n |INGREDIENTES| \n -------------")
                    for ingrediente in plato.listaDeIngredientes:
                        print(f"Ingrediente \t Cantidad \t Unidad de medida \n {ingrediente.nombre} \t\t {ingrediente.cantidad} \t\t {ingrediente.unidadDeMedida} \n ---------------------------------------") 

def main():             
    menu = MenuRestaurant()
    menu.agregar_plato()
    menu.mostrar_menu()
if __name__  == "__main__":
    main()
