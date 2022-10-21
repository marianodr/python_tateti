from tateti import Tateti
from os import system , name
from time import sleep
from readchar import readkey

def iniciar():
    # Bienvenida al jugador
    nombreJugador = bienvenida()
    
    # Breve introduccion
    instrucciones(nombreJugador)
    
    # Seleccion del nivel de dificultad
    nivel = dificultad()

    # Inicio del juego
    inicioJuego(nombreJugador, nivel)

def bienvenida(): # Mensaje de bienvenida
    system('cls' if name == 'nt' else 'clear')

    print("\t\t\t\tBienvenido a TATETI!")
    sleep(1)

    print("\nMe presento, mi nombre es Tateti-800, y voy a jugar contigo.")
    sleep(3)

    nombreJugador = input("\n¿Cual es tu nombre?: ---> ")

    return nombreJugador

def instrucciones(nombreJugador): # Breve explicacion de las coordenadas
    system('cls' if name == 'nt' else 'clear')

    print("\nHola " + nombreJugador + "! Supongo que ya sabes como jugar a TATETI...")
    sleep(3)
    print("\nSolo te dare una aclaracion:")
    sleep(2)
    print("\nCuando es tu turno, debes ingresar el numero de la celda que deseas poner tu 'ficha', a traves de tu teclado numerico.")
    sleep(5)
    print("\nEstas son las coordenadas!\n")

    sleep(2)
    print("\t\t\t| 7 | 8 | 9 |")
    print("\t\t\t____________")
    print("\t\t\t| 4 | 5 | 6 |")
    print("\t\t\t____________")
    print("\t\t\t| 1 | 2 | 3 |")

    sleep(4)
    print("\nEstas listo? Presiona una tecla para comenzar...")
    readkey()

def dificultad(): # Nivel de dificultad del Agente
    nivel = 0
    while not nivel in ('1', '2', '3'):
        system('cls' if name == 'nt' else 'clear')
        print("\nPrimero, elige un nivel de dificultad")
        print("1. Facil")
        print("2. Medio")
        print("3. Dificil") 
        
        print("\nIngresa una opcion: --->  ", end = '')
        nivel = readkey()

def inicioJuego(nombreJugador, nivel): # Inicio de las partidas de TaTeTi
    while True:
        tateti = Tateti(nombreJugador, nivel)
        tateti.jugar()

        op = 0
        while not op in ('1', '2'):
            print("\nDeseas jugar nuevamente?")
            print("1. Si")
            print("2. No") 
            
            print("\nIngresa una opcion: --->  ", end = '')
            op = readkey()
            system('cls' if name == 'nt' else 'clear')
            
        if op == '2': 
            break

if __name__ == '__main__':
    iniciar()
