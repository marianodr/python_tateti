from jugadorBase import JugadorBase
from readchar import readkey

class Jugador(JugadorBase):
    def __init__(self, nombre):
        super().__init__(nombre)

    def jugar(self, tablero):
        print(f"\nEs tu turno {self.nombre}, ingresa una coordenada --->  ", end = '')
        
        while True:
            op = readkey()
            
            if not op in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("\nIngresa una coordenada valida!")
                continue
            
            if tablero.contenidoCelda(int(op) - 1) == None: # Se resta 1 porque los id de las celdas empiezan en 0
                tablero.modificarCelda(int(op) - 1, 'x')
                break
            
            else:
                tablero.mostrar()
                print("\nEsa coordenada ya esta ocupada! Intenta otra...")
                continue
        
        # Actualiza su estado de ganador (True or False)
        self.ganador = self.victoria(tablero, 'x')