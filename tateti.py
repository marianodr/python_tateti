from tablero import Tablero
from jugador import Jugador
from agente import Agente

class Tateti:
    idTateti = 0
    historial = {"jugador":0 , "agente":0, "empates":0}

    def __init__(self, nombreJugador, nivel) -> None:
        __class__.idTateti += 1
        self.__idTateti = __class__.idTateti
        self.__tablero = Tablero()
        self.__jugador = Jugador(nombreJugador)
        self.__agente = Agente("Tateti-800", nivel)

    def jugar(self):
        if self.__idTateti % 2 == 1: # Permite alternar quien comienza el juego
            principal = self.__jugador
            auxiliar = self.__agente
        else:
            principal = self.__agente
            auxiliar = self.__jugador

        while True:
            self.__tablero.mostrar()
            
            # Turno del jugador
            principal.jugar(self.__tablero)
            self.__tablero.mostrar()

            # Se verifica si es el fin del juego
            if self.__tablero.completo() or principal.ganador:
                break

            # Turno del agente
            auxiliar.jugar(self.__tablero)

            # Se verifica si es el fin del juego
            if self.__tablero.completo() or auxiliar.ganador:
                self.__tablero.mostrar()
                break

        # Se realiza una distincion para imprimir el mensaje correcto y contar el resultado del juego
        if self.__idTateti % 2 == 1:
            if principal.ganador:
                print("\nFelicidades, has ganado!")
                __class__.historial["jugador"] += 1
            elif auxiliar.ganador:
                print("\nPerdiste! Jajaja")
                __class__.historial["agente"] += 1
            else:
                print("\nEmpate...")
                __class__.historial["empates"] += 1
        else:
            if principal.ganador:
                print("\nPerdiste! Jajaja")
                __class__.historial["agente"] += 1
            elif auxiliar.ganador:
                print("\nFelicidades, has ganado!")
                __class__.historial["jugador"] += 1
            else:
                print("\nEmpate...")
                __class__.historial["empates"] += 1

        print("\n", 17 * "- ")
        print(f"Victorias de {self.__jugador.nombre}: ", __class__.historial["jugador"])
        print(f"Victorias de {self.__agente.nombre}: ", __class__.historial["agente"])
        print(f"Empates: ", __class__.historial["empates"], "\n")