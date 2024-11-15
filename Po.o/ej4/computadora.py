class Computadora:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.listadeobjetosComponenteCPU = []
    def agregar_componente(self,componente):
        self.listadeobjetosComponenteCPU.append(componente)
