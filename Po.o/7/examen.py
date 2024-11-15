
from Filtrar_equipo import Equipo
personajes_principales = [
    ("Pipo", 239, "Rogue", "GRAGAS", 3, False),
    ("Shinra", 40, "Cleric", "Half-Elf", 5, False),
    ("fran", 25, "Warlock", "Human", 2, False),
    ("jere", 35, "Wizard", "Human", 5, False),
    ("Tomi", 32, "Barbarian", "Tiefling", 6, False),
    ("Valen", 20, "Fighter", "Githyanki", 4, False),
    ("Gero", 150, "Druid", "Dovakin", 9, False),
    ("Lucho", 350, "Druid", "Elf", 7, False),
    ("Delfi", 130, "Ranger", "Human", 5, False),
    ("Espetxe", 250, "Paladin", "ENTERRADOR", 8, False),
    ("Hernan", 30, "Sorcerer", "Dragonborn", 7, False)
]
class menu:
    def __init__(self):
        self.equipo = []
    
    def filtrar_equipo(self, personajes):
        while len(self.equipo) < 5:
            nombres_personajes = [i[0] for i in personajes]
            mi_equipo = input(f"Ingrese el nombre del personaje que desea tener en su equipo: \n {nombres_personajes}\n")

            if mi_equipo not in nombres_personajes:
                print("No existe el personaje.")
                continue
            
            if any(pj.nombre == mi_equipo for pj in self.equipo):
                print("Este personaje ya está en su equipo.")
                continue
            
            for i in personajes:
                if i[0] == mi_equipo:
                    pj1 = Equipo(i[0], i[1], i[2], i[3], i[4])
                    self.equipo.append(pj1)  # Aquí es donde se añade el personaje
                    print(f"{mi_equipo} ha sido añadido a su equipo.")
                    break 
        return self.equipo
    def nivel_medio(self):
        suma = 0
        cont = 0
        for i in self.equipo:
                suma += i.nivel
                cont += 1
        media = suma / cont

    def mostrar_equipo(self):
        for i in self.equipo:
            print(f"Nombre: \t {i.nombre}\n edad\t\tClase\t\tRaza\t\tNivel \n------------------------\n\t{i.edad}\t\t{i.clase}\t\t{i.raza}\t\t{i.nivel}\n")
def main():
    mi_menu = menu()
    shinra = mi_menu.filtrar_equipo(personajes_principales)
    print("-------------------")
    mi_menu.mostrar_equipo()
    print(f"promedio de nivel de tu equipo: {mi_menu.nivel_medio()}")

if __name__ ==  "__main__":
    main()
