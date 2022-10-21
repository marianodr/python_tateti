from jugadorBase import JugadorBase
from random import randint
from time import sleep
from random import choice

class Agente(JugadorBase):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.__nivel = nivel

    # Metodos privados
    def __turnosJugados(self, tablero, simbolo) -> int: # Cuenta los turnos jugados por el agente o el jugador
        turnos = 0

        for i in range(9):
            if tablero.contenidoCelda(i) == simbolo:
                turnos += 1

        return turnos

    def __mejorMovimiento(self, tablero, simbolo) -> int or None: # Retorna la coordenada del movimiento ganador o que bloquea al jugador
        # Analiza las posibilidades ganadoras
        # Fila 1
        if tablero.contenidoCelda(1) == simbolo and tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(0) == None:
            return 0
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(1) == None:
            return 1
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(1) == simbolo and tablero.contenidoCelda(2) == None:
            return 2
        
        # Fila 2
        elif tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(5) == simbolo and tablero.contenidoCelda(3) == None:
            return 3
        elif tablero.contenidoCelda(3) == simbolo and tablero.contenidoCelda(5) == simbolo and tablero.contenidoCelda(4) == None:
            return 4
        elif tablero.contenidoCelda(3) == simbolo and tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(5) == None:
            return 5

        # Fila 3
        elif tablero.contenidoCelda(7) == simbolo and tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(6) == None:
            return 6
        elif tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(7) == None:
            return 7
        elif tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(7) == simbolo and tablero.contenidoCelda(8) == None:
            return 8
        
        # Columna 1
        elif tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(3) == simbolo and tablero.contenidoCelda(0) == None:
            return 0
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(3) == None:
            return 3
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(3) == simbolo and tablero.contenidoCelda(6) == None:
            return 6
        
        # Columna 2
        elif tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(7) == simbolo and tablero.contenidoCelda(1) == None:
            return 1
        elif tablero.contenidoCelda(1) == simbolo and tablero.contenidoCelda(7) == simbolo and tablero.contenidoCelda(4) == None:
            return 4
        elif tablero.contenidoCelda(1) == simbolo and tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(7) == None:
            return 7

        # Columna 3
        elif tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(5) == simbolo and tablero.contenidoCelda(2) == None:
            return 2
        elif tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(5) == None:
            return 5
        elif tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(5) == simbolo and tablero.contenidoCelda(8) == None:
            return 8
        
        # Diagonal Principal
        elif tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(2) == None:
            return 2
        elif tablero.contenidoCelda(6) == simbolo and tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(4) == None:
            return 4
        elif tablero.contenidoCelda(2) == simbolo and tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(6) == None:
            return 6

        # Diagonal Secundaria
        elif tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(0) == None:
            return 0
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(8) == simbolo and tablero.contenidoCelda(4) == None:
            return 4
        elif tablero.contenidoCelda(0) == simbolo and tablero.contenidoCelda(4) == simbolo and tablero.contenidoCelda(8) == None:
            return 8
        
        else:
            return None

    def __jugarObligado(self, tablero) -> int or None: # Casos particulares no evidentes que suponen amenaza futura
        if tablero.contenidoCelda(4) == 'o': # 8 casos particulares que imponen restricciones
            if (tablero.contenidoCelda(0) == 'x' and tablero.contenidoCelda(5) == 'x') or (tablero.contenidoCelda(6) == 'x' and tablero.contenidoCelda(5) == 'x'):
                return choice((1, 2, 7, 8)) # 1, 2, 7, 8
            elif (tablero.contenidoCelda(1) == 'x' and tablero.contenidoCelda(6) == 'x') or (tablero.contenidoCelda(1) == 'x' and tablero.contenidoCelda(8) == 'x'):
                return choice((0, 2, 3, 5)) # 0, 2, 3 o 5
            elif (tablero.contenidoCelda(2) == 'x' and tablero.contenidoCelda(7) == 'x') or (tablero.contenidoCelda(0) == 'x' and tablero.contenidoCelda(7) == 'x'):
                return choice((3, 5, 6, 8)) # 3, 5, 6 o 8
            elif (tablero.contenidoCelda(8) == 'x' and tablero.contenidoCelda(3) == 'x') or (tablero.contenidoCelda(2) == 'x' and tablero.contenidoCelda(3) == 'x'):
                return choice((0, 1, 6, 7)) # 0, 1, 6 o 7
            else:
                return None

        return None

    def __jugarEsquina(self, tablero):
        esquinas = self.__esquinasDisponibles(tablero)

        if esquinas != None:
            tablero.modificarCelda(choice(esquinas), 'o')
            return True
        else:
            return False

    def __esquinasDisponibles(self, tablero):
        return [e for e in (0, 2, 6, 8) if tablero.contenidoCelda(e) == None]

    def __jugarCentro(self, tablero) -> bool: # Asegura el centro si esta disponible
        if tablero.contenidoCelda(4) == None:
            tablero.modificarCelda(4, 'o')
            return True

    def __jugarAleatorio(self, tablero):
        coordenada = randint(0,8)
        if tablero.contenidoCelda(coordenada) == None:
            tablero.modificarCelda(coordenada, 'o')
            return True

    # Metodos publicos
    def jugar(self, tablero):
        print(f"\n(Es el turno de {self.nombre}. Espera, esta pensando...)")
        sleep(2)

        # Nivel Facil
        while True:
            if self.__nivel == '1': # Nivel Facil
                # Asegura el centro si esta disponible
                if self.__jugarCentro(tablero):
                    break
            
                if self.__jugarAleatorio(tablero):
                    break
                
            elif self.__nivel == '2': # Nivel Medio
                # Asegura el centro si esta disponible
                if self.__jugarCentro(tablero):
                    break
                
                # Juega alguna esquina
                if self.__turnosJugados(tablero, 'o') <= 2:
                    if self.__jugarEsquina(tablero):
                        break
                        
                if self.__jugarAleatorio(tablero):
                    break
                
            else: # Nivel Dificil
                # Asegura el centro si esta disponible
                if self.__jugarCentro(tablero):
                    break
                    
                # Analiza la posibilidad de ganar
                if self.__turnosJugados(tablero, 'o')>=2:
                    mejorMovimiento = self.__mejorMovimiento(tablero, 'o')
                    
                    if mejorMovimiento != None:
                        tablero.modificarCelda(mejorMovimiento, 'o')
                        break  
                
                # Analiza la posibilidad de tapar una jugada rival
                if self.__turnosJugados(tablero, 'x')>=2: 
                    mejorMovimiento = self.__mejorMovimiento(tablero, 'x')
                    
                    if mejorMovimiento != None:
                        tablero.modificarCelda(mejorMovimiento, 'o')
                        break
                
                # Juega alguna esquina
                if self.__turnosJugados(tablero, 'o') <= 1 and self.__turnosJugados(tablero, 'x') <= 1 and self.__jugarEsquina(tablero):
                    break
            
                # Analiza el caso de jugadas obligatorias/riesgosas
                if self.__turnosJugados(tablero, 'o') == 1 and self.__turnosJugados(tablero, 'x') == 2:
                    jugadaObligatoria = self.__jugarObligado(tablero) 

                    if jugadaObligatoria != None:
                        tablero.modificarCelda(jugadaObligatoria, 'o')
                        break

                # Si no se cumple ninguna de las condiciones anteriores, juega un casillero de manera aleatoria
                if self.__jugarAleatorio(tablero):
                    break
                
        # Actualiza su estado de ganador (True or False)
        self.ganador = self.victoria(tablero, 'o')

