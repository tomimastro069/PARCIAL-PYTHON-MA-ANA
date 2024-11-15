class Alumno:
    def __init__(self, nombre_completo, legajo):
        self.nombre_completo = nombre_completo
        self.legajo = legajo
        self.lista_notas = []

    def cargar_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_promedio(self):
        if not self.lista_notas:
            return 0
        total = sum(nota.nota_examen for nota in self.lista_notas)
        return total / len(self.lista_notas)