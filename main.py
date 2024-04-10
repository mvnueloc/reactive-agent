import pygame
import random
import math
#Practica 1 - Agentes Reactivos

# Inicializar motor de pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("P.1 Agentes Reactivos")

# Sonido de fondo
#sonido_fondo = pygame.mixer.Sound('static/sound.wav')
#pygame.mixer.Sound.play(sonido_fondo, -1) # Con -1 indicamos que queremos que se repita indefinidamente


# Cargar imagenes
# <--- Objetos --->
background = pygame.image.load('static/background.png')
zombie = pygame.image.load('static/zombie1.png')
zombie_comido = pygame.image.load('static/zombie_comido.png')
tumba = pygame.image.load('static/tumba.png')
cerebro = pygame.image.load('static/cerebro.png')
obstaculo = pygame.image.load('static/obstaculo.png')
# <--- Botones --->
botton_brain = pygame.image.load('static/button_brains1.png')
botton_obstaculo = pygame.image.load('static/button_obstacle.png')
button_trasher = pygame.image.load('static/button_trasher.png')
button_zombie = pygame.image.load('static/button_zombie.png')
button_tumba = pygame.image.load('static/button_tumba.png')
# <--- Botones ON --->
botton_brain_on = pygame.image.load('static/button_brains1_on.png')
botton_obstaculo_on = pygame.image.load('static/button_obstacle_on.png')
button_trasher_on = pygame.image.load('static/button_trasher_on.png')
button_zombie_on = pygame.image.load('static/button_zombie_on.png')
button_tumba_on = pygame.image.load('static/button_tumba_on.png')


# Escalar imagenes
zombien = pygame.transform.scale(zombie, (50, 50))
zombie_comido =  pygame.transform.scale(zombie_comido,(50,50))
tumban = pygame.transform.scale(tumba, (60, 60))
cerebro = pygame.transform.scale(cerebro, (40, 40))
background = pygame.transform.scale(background, (500, 500))
obstaculo = pygame.transform.scale(obstaculo, (50, 50))
botton_brain = pygame.transform.scale(botton_brain, (100, 40))
botton_obstaculo = pygame.transform.scale(botton_obstaculo, (100, 40))
button_trasher = pygame.transform.scale(button_trasher, (50, 40))
botton_brain_on = pygame.transform.scale(botton_brain_on, (100, 40))
botton_obstaculo_on = pygame.transform.scale(botton_obstaculo_on, (100, 40))
button_trasher_on = pygame.transform.scale(button_trasher_on, (50, 40))
button_zombie = pygame.transform.scale(button_zombie, (50, 40))
button_tumba = pygame.transform.scale(button_tumba, (50, 40))
button_zombie_on = pygame.transform.scale(button_zombie_on, (50, 40))
button_tumba_on = pygame.transform.scale(button_tumba_on, (50, 40))

# Coordenadas para botones
espacio_botones = 20

coordenadas_botones = [[(0,0),(25,0 + espacio_botones),(100, 0 + espacio_botones),(150,0),(225,0 + espacio_botones),(250,0),(300,0 + espacio_botones),(350,0),(400,0 ),(425,0 + espacio_botones)],]

# Brain -> 0,2
# Obstaculo -> 0,6
# Trash -> 0,4

# Matriz de coordenadas para objetos
coordenadas = [
               [(0,100),(50,100),(100,100),(150,100),(200,100),(250,100),(300,100),(350,100),(400,100),(450,100)],
               [(0,150),(50,150),(100,150),(150,150),(200,150),(250,150),(300,150),(350,150),(400,150),(450,150)],
               [(0,200),(50,200),(100,200),(150,200),(200,200),(250,200),(300,200),(350,200),(400,200),(450,200)],
               [(0,250),(50,250),(100,250),(150,250),(200,250),(250,250),(300,250),(350,250),(400,250),(450,250)],
               [(0,300),(50,300),(100,300),(150,300),(200,300),(250,300),(300,300),(350,300),(400,300),(450,300)],
               [(0,350),(50,350),(100,350),(150,350),(200,350),(250,350),(300,350),(350,350),(400,350),(450,350)],
               [(0,400),(50,400),(100,400),(150,400),(200,400),(250,400),(300,400),(350,400),(400,400),(450,400)],
               [(0,450),(50,450),(100,450),(150,450),(200,450),(250,450),(300,450),(350,450),(400,450),(450,450)]]

# Aqui apareceran los todos los elementos con zombies moviendose aleatoriamente
tablero = [['','','','','','','','','',''],
           ['','','','','','','','','',' '],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','','']]


# Tablero de coordenadas para zombies que ya comieron un cerebro
# Aqui apareceran los todos los elementos con zombies moviendose aleatoriamente
tablero_zc = [['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','',''],
              ['','','','','','','','','','']]

# Funcion mostrar matriz
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print('--------------------------------')


# Variable si ya termino el juego
game_over = False

# Fps
clock = pygame.time.Clock()

fil_tumba = 0
col_tumba = 0


# Funcion para graficar objetos
def graficar_objetos():
    screen.blit(background, (0, 0)) #Fondo

    for fil in range(8):
        for col in range(10):

            # Graficar botones
            if poner_cerebro:
                screen.blit(botton_brain_on, coordenadas_botones[0][2])
            else:
                screen.blit(botton_brain, coordenadas_botones[0][2])
            if poner_obstaculo:
                screen.blit(botton_obstaculo_on, coordenadas_botones[0][6])
            else:
                screen.blit(botton_obstaculo, coordenadas_botones[0][6])
            if borrar_objeto:
                screen.blit(button_trasher_on, coordenadas_botones[0][4])
            else:
                screen.blit(button_trasher, coordenadas_botones[0][4])
            if poner_zombie:
                screen.blit(button_zombie_on, coordenadas_botones[0][1])
            else:
                screen.blit(button_zombie, coordenadas_botones[0][1])
            if poner_tumba:
                screen.blit(button_tumba_on, coordenadas_botones[0][9])
            else:
                screen.blit(button_tumba, coordenadas_botones[0][9])
            
            
            # Graficar objetos
            if tablero_zc[fil][col] == 'zc':
                screen.blit(zombie_comido,coordenadas[fil][col])
            elif tablero[fil][col] == 'z':
                screen.blit(zombien, coordenadas[fil][col])
            elif tablero[fil][col] == 't':
                screen.blit(tumban, coordenadas[fil][col])
            elif tablero[fil][col] == 'c':
                screen.blit(cerebro, coordenadas[fil][col])
            elif tablero[fil][col] == 'o':
                screen.blit(obstaculo, coordenadas[fil][col])

# Regresar los zm a z
def regresar_zm_a_z():
    for fil in range(8):
        for col in range(10):
            if tablero[fil][col] == 'zm':
                tablero[fil][col] = 'z'

# Movimiento aleatorio zombies
def mover_zombies():
    for fil in range(8): 
        for col in range(10):
            if tablero[fil][col] == 'z':
                
                num_aleatorio = random.randint(0, 3)
                
                if num_aleatorio == 0:
                    print('Movimiento: Arriba')
                elif num_aleatorio == 1:
                    print('Movimiento: Abajo')
                elif num_aleatorio == 2:
                    print('Movimiento: Izquierda')
                elif num_aleatorio == 3:
                    print('Movimiento: Derecha')

                if num_aleatorio == 0: #movimiento arriba
                    if fil - 1 >= 0 and tablero[fil-1][col] != 'z' and tablero[fil-1][col] != 't' and tablero[fil-1][col] != 'o' and tablero[fil-1][col] != 'zm':
                        
                        if tablero[fil - 1][col] == 'c':
                            tablero[fil][col] = ''
                            tablero[fil-1][col] = ''
                            tablero_zc[fil-1][col] = 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col] = ''
                            tablero[fil - 1][col] = 'zm'

                elif num_aleatorio == 1: #movimiento abajo
                    if fil + 1 <= 7 and tablero[fil+1][col] != 'z' and tablero[fil+1][col] != 't' and tablero[fil+1][col] != 'o' and tablero[fil+1][col] != 'zm':
                        
                        if tablero[fil + 1][col] == 'c':
                            tablero[fil][col] = ''
                            tablero[fil+1][col] = ''
                            tablero_zc[fil+1][col] = 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col] = ''
                            tablero[fil + 1][col] = 'zm'

                elif num_aleatorio == 2: #movimiento izquierda
                    if col - 1 >= 0 and tablero[fil][col-1] != 'z' and tablero[fil][col-1] != 't' and tablero[fil][col-1] != 'o' and tablero[fil][col-1] != 'zm':
                        

                        if tablero[fil][col-1] == 'c':
                            tablero[fil][col] = ''
                            tablero[fil][col-1] = ''
                            tablero_zc[fil][col-1] = 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col] = ''
                            tablero[fil][col - 1] = 'zm'


                elif num_aleatorio == 3: #movimiento derecha
                    if col + 1 <= 9 and tablero[fil][col+1] != 'z' and tablero[fil][col+1] != 't' and tablero[fil][col+1] != 'o' and tablero[fil][col+1] != 'zm':
                        
                        
                        if tablero [fil][col+1] == 'c':
                            tablero[fil][col+1] = ''
                            tablero[fil][col] = ''
                            tablero_zc[fil][col+1] = 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col] = ''
                            tablero[fil][col + 1] = 'zm'

    for fil in range(8):
        for col in range(10):
            if tablero[fil][col] == 'zm':
                tablero[fil][col] = 'z'



def moviemiento_zombie_comido ():
    for fil in range(8):
        for col in range(10):
            
            if tablero_zc[fil][col] == 'zc':

                # existe arriba?
                if fil != 0 and tablero[fil-1][col] != 'o':
                    # distancia euclidiana a la tumba
                    arriba_a_tuba = math.sqrt((fil_tumba - (fil-1))**2 + (col_tumba - col)**2)
                else:
                    arriba_a_tuba = 1000000;

                # existe abajo?
                if fil != 7 and tablero[fil+1][col] != 'o':
                    # distancia euclidiana a la tumba
                    abajo_a_tuba = math.sqrt((fil_tumba - (fil+1))**2 + (col_tumba - col)**2)
                else:
                    abajo_a_tuba = 1000000;

                # existe izquierda?
                if col != 0 and tablero[fil][col-1] != 'o':
                    # distancia euclidiana a la tumba
                    izquierda_a_tuba = math.sqrt((fil_tumba - fil)**2 + (col_tumba - (col-1))**2)
                else:
                    izquierda_a_tuba = 1000000;

                # existe derecha?
                if col != 9 and tablero[fil][col+1] != 'o':
                    # distancia euclidiana a la tumba
                    derecha_a_tuba = math.sqrt((fil_tumba - fil)**2 + (col_tumba - (col+1))**2)
                else:
                    derecha_a_tuba = 1000000;
                
                # Nos quedamos con la distancia mas corta
                minimo = min(arriba_a_tuba, abajo_a_tuba, izquierda_a_tuba, derecha_a_tuba)

                if minimo == arriba_a_tuba:
                    if tablero[fil-1][col] == 't':
                        tablero_zc[fil][col] = ''
                        tablero[fil][col] = 'z'
                        print('Zombie ha llegado a la tumba y se convierte en zombie normal')
                    else:
                        tablero_zc[fil][col] = ''
                        tablero_zc[fil-1][col] = 'zcm'
                        print('Zombie comido se mueve arriba')

                elif minimo == abajo_a_tuba:
                    if tablero[fil+1][col] == 't':
                        tablero_zc[fil][col] = ''
                        tablero[fil][col] = 'z'
                        print('Zombie ha llegado a la tumba y se convierte en zombie normal')
                    else:
                        tablero_zc[fil][col] = ''
                        tablero_zc[fil+1][col] = 'zcm'
                        print('Zombie comido se mueve abajo')

                elif minimo == izquierda_a_tuba:
                    if tablero[fil][col-1] == 't':
                        tablero_zc[fil][col] = ''
                        tablero[fil][col] = 'z'
                        print('Zombie ha llegado a la tumba y se convierte en zombie normal')
                    else:
                        tablero_zc[fil][col] = ''
                        tablero_zc[fil][col-1] = 'zcm'
                        print('Zombie comido se mueve izquierda')

                elif minimo == derecha_a_tuba:
                    if tablero[fil][col+1] == 't':
                        tablero_zc[fil][col] = ''
                        tablero[fil][col] = 'z'
                        print('Zombie ha llegado a la tumba y se convierte en zombie normal')
                    else:
                        tablero_zc[fil][col] = ''
                        tablero_zc[fil][col+1] = 'zcm'
                        print('Zombie comido se mueve derecha')

    for fil in range(8):
        for col in range(10):
            if tablero_zc[fil][col] == 'zcm':
                tablero_zc[fil][col] = 'zc'

poner_cerebro = False
poner_obstaculo = False
poner_zombie = False
poner_tumba = False
borrar_objeto = False


# Agregar cerebro
def agregar(x, y, tipo):
    if tablero[x][y] == '':
        tablero[x][y] = tipo
                
# Loop de juego
while not game_over:
    clock.tick(10) #Siempre corra a 30 fps

    for event in pygame.event.get(): #Obtener eventos
        if event.type == pygame.QUIT: #Si el evento es cerrar la ventana
            game_over = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = event.pos
            print('[Click] ',x, y)

            #Botones con coordenadas no dinamicas si se cambia la posicion de los botones buggea
            if x >= 100 and x <= 200 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones): 
                print('[Cerebro]')

                if poner_cerebro:
                    poner_cerebro = False
                else:
                    poner_cerebro = True
                    poner_obstaculo = False
                    borrar_objeto = False
                    poner_zombie = False
                    poner_tumba = False

            elif x >= 300 and x <= 400 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Obstaculo]')

                if poner_obstaculo:
                    poner_obstaculo = False
                else:
                    poner_obstaculo = True
                    poner_cerebro = False
                    borrar_objeto = False
                    poner_zombie = False
                    poner_tumba = False

            elif x >= 225 and x <= 275 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Trash]')

                if borrar_objeto:
                    borrar_objeto = False
                else:
                    borrar_objeto = True
                    poner_cerebro = False
                    poner_obstaculo = False
                    poner_tumba = False
                    poner_zombie = False
                    
            
            elif x >= 25 and x <= 75 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Zombie]')

                if poner_zombie:
                    poner_zombie = False
                else:
                    poner_zombie = True
                    poner_tumba = False
                    poner_obstaculo = False
                    poner_cerebro = False
                    borrar_objeto = False
            
            elif x >= 425 and x <= 475 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Tumba]')

                if poner_tumba:
                    poner_tumba = False
                else:
                    poner_tumba = True
                    poner_zombie = False
                    poner_obstaculo = False
                    poner_cerebro = False
                    borrar_objeto = False

            elif poner_cerebro and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                print('Coordenadas: ', x, y)
                agregar(y, x, 'c')
            elif poner_obstaculo and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                agregar(y, x, 'o')

            elif borrar_objeto and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                tablero[y][x] = ''

            elif poner_zombie and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                agregar(y, x, 'z')
            elif poner_tumba and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                fil_tumba, col_tumba = y, x
                agregar(y, x, 't')

            # Se le resta 100 por que no contamos el rango de los botones
            # Se mandan las coordenadas en orden inverso ya que el eje x y y estan al reves
            # en la matriz de coordenadas y en la matriz del tablero, por como se ven los pixeles 
            # y las matrices


    mover_zombies()

    moviemiento_zombie_comido()

    graficar_objetos()

    # Actualizar pantalla
    pygame.display.update()


pygame.quit() #Cerrar el juego