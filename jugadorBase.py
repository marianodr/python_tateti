class JugadorBase():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ganador = False

    @property
    def nombre(self):
        return self.__nombre

    @property
    def ganador(self):
        return self.__ganador

    @ganador.setter
    def ganador(self, ganador):
        self.__ganador = ganador

    def jugar(self, tablero):
        pass

    def victoria(self, tablero, simbolo) -> bool:
        # Identifica si existe una fila, columna o diagonal con el mismo contenido  para determinar si el jugador gano
        for i in range(3):
            # Columnas:
            if tablero.contenidoCelda(i) == tablero.contenidoCelda(i + 3) == tablero.contenidoCelda(i + 6) == simbolo:
                return True
            
            # Filas:
            if tablero.contenidoCelda(i * 3) == tablero.contenidoCelda(i * 3 + 1) == tablero.contenidoCelda(i * 3 + 2) == simbolo:
                return True
            
        # Diagonales:
        if tablero.contenidoCelda(0) == tablero.contenidoCelda(4) == tablero.contenidoCelda(8) == simbolo:
            return True
        elif tablero.contenidoCelda(2) == tablero.contenidoCelda(4) == tablero.contenidoCelda(6) == simbolo:
            return True
        else:
            return False