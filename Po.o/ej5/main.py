from claseBarrio import Barrio

from ClaseHabitacion import  Habitacion

from ClaseVivienda import  Vivienda


def main():

    barrio = Barrio("alto challao","XYP")
    Vivienda1 =  Vivienda("santa rita","2","K","4",500)
    Vivienda2 = Vivienda("Santa rita","2","J","5",450)
    Vivienda1.agregar_habitacion(Habitacion("Pieza 1", 30.0))
    Vivienda2.agregar_habitacion(Habitacion("Baño", 15.0))
    

    
    barrio.agregar_vivienda(Vivienda1)
    barrio.agregar_vivienda(Vivienda2)

    print(f"Barrio\t\tConstructora\n{barrio.nombre}\t{barrio.empresaConstructora}")
    print("---------------------")

    for i in barrio.ListaDeObjetosVivienda:
        print(f"Vivienda\n--------\n\tCalle\t\tNumero\tManzana\tNroCasa\tSuperfecie\n \t{i.calle}\t{i.numero}\t{i.manzana}\t{i.nrocasa}\t{i.superficieTerreno}")
        for j in  i.ListaObjHabitacion:
            print(f"Habitacion\n--------\n\tNombre\tSuperficie\n\t{j.nombre}\t{j.metrosCuadrados}")
                  

    print(f"Superficie total de terreno en el barrio: {barrio.getSuperficieTotalTerreno()} m²")
    print(f"Superficie total de terreno en la manzana A: {barrio.getSuperficieTotalTerrenoXManzana('A')} m²")
    print(f"Superficie total cubierta en el barrio: {barrio.getSuperficieTotalCubierta()} m²")

if __name__ == "__main__":
    main()
