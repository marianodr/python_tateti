from celda import Celda
from os import system, name

class Tablero:
    def __init__(self) -> None:
        self.__celdas = self.__generarCeldas()

    # Metodos privados
    def __generarCeldas(self) -> list:
        return  [Celda() for c in range(9)]

    # Metodos publicos
    def mostrar(self): # Imprime el tablero
        system('cls' if name == 'nt' else 'clear')
        print("Tablero actual\t\t\tCoordenadas")
        print("|", self.__celdas[6], self.__celdas[7], self.__celdas[8], "\t\t\t| 7 | 8 | 9 |")
        print("_____________")
        print("|", self.__celdas[3], self.__celdas[4], self.__celdas[5], "\t\t\t| 4 | 5 | 6 |")
        print("_____________")
        print("|", self.__celdas[0], self.__celdas[1], self.__celdas[2], "\t\t\t| 1 | 2 | 3 |")

    def completo(self) -> bool:
        for celda in self.__celdas:
            if celda.contenido == None:
                return False
        return True

    def contenidoCelda(self, coordenada) -> str:
        return self.__celdas[coordenada].contenido

    def modificarCelda(self, coordenada, simbolo):
        self.__celdas[coordenada].contenido = simbolo