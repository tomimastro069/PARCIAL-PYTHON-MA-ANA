from claseAlumno import Alumno
from clasenota import Nota

class CargarNotas:
    def __init__(self):
        self.alumnos = []

    def cargar_alumno(self):
        while True:
            nombre = input("Ingrese el nombre del alumno: ")
            legajo = int(input("Ingrese el legajo del alumno: "))
            alumno = Alumno(nombre, legajo)
            cant_notas = int(input(f"Ingrese la cantidad de notas del alumno {alumno.nombre_completo}: "))
            if cant_notas <= 0:
                print("La cantidad de notas debe ser mayor a 0")
            catedra = input(f"Ingrese la cátedra de la nota para {alumno.nombre_completo}: ")
            for i in range(cant_notas):
                nota_valor = float(input(f"Ingrese la nota número {i + 1} para {alumno.nombre_completo}: "))
                nota_obj = Nota(catedra, nota_valor)
                alumno.cargar_nota(nota_obj) 

            self.alumnos.append(alumno)  

            continuar = input("¿Desea ingresar otro alumno? (s/n): ")
            if continuar.lower() == "n":
                break

    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(f"Alumno \t Legajo \t promedio \n{alumno.nombre_completo} \t  {alumno.legajo} \t\t {alumno.calcular_promedio()}\n ---------------------------------------------")

def main():
    cargador = CargarNotas()
    cargador.cargar_alumno() 
    cargador.mostrar_informacion()

if __name__ == "__main__":
    main()