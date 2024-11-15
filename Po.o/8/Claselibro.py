class libro:
    def __init__(self,titulo,autor,año_publicacion,genero):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
    def Mostrar_info(self):
        return print(f"Hola, el libro es: {self.titulo} de {self.autor}, publicado en {self.año_publicacion} y pertenece al género de {self.genero}")