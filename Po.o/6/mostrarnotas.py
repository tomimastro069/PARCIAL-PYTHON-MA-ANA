from claseAlumno import Alumno
class notasalumno:
    def __init__(self):
        self.notas = []
    def cargarNotasAlumno(self):
        while True:
            nombre = input("Ingrese el nombre del alumno: ")
            dni = int(input("Ingrese el dni del alumno: "))
            cantidadnota = int(input("Ingrese la cantidad de  notas que desea agregar: "))
            totalNota = 0
            for i in range(cantidadnota):
                nota = float(input(f"Ingrese la nota {i+1} del alumno: "))
                totalNota += nota
            promedio =  totalNota / cantidadnota
            alumno = Alumno(nombre,dni,promedio)
            self.notas.append(alumno)
            continuar = input("¿Desea ingresar otro alumno? (s/n): ")
            if continuar.lower() == "n":
                break
    def mostrar_informacion(self):
        for alumno in self.notas:
            print(f"\nPROMEDIO\nAlumno\t Dni\t  Promedio Final\n{alumno.nombre}\t{alumno.dni}\t\t{alumno.promedio}")
def main():
    notas = notasalumno()
    notas.cargarNotasAlumno()
    notas.mostrar_informacion()
if __name__  == "__main__":
    main()




                


            
            

