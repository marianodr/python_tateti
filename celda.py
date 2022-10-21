class Celda:
    def __init__(self):
        self.__contenido = None

    @property
    def contenido(self):
        return self.__contenido

    @contenido.setter
    def contenido(self, contenido):
        self.__contenido = contenido

    def __str__(self):
        return f'{self.__contenido} |' if self.__contenido != None else '  |'