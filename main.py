import pygame
import random


# Inicializar motor de pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("P.1 Agentes Reactivos")

# Sonido de fondo
sonido_fondo = pygame.mixer.Sound('static/sound.wav')
pygame.mixer.Sound.play(sonido_fondo, -1) # Con -1 indicamos que queremos que se repita indefinidamente


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
# <--- Botones ON --->
botton_brain_on = pygame.image.load('static/button_brains1_on.png')
botton_obstaculo_on = pygame.image.load('static/button_obstacle_on.png')
button_trasher_on = pygame.image.load('static/button_trasher_on.png')


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

# Coordenadas para botones
espacio_botones = 20

coordenadas_botones = [[(0,0),(50,0),(100, 0 + espacio_botones),(150,0),(225,0 + espacio_botones),(250,0),(300,0 + espacio_botones),(350,0),(400,0),(450,0)],
                       [(0,50),(50,50),(100,50),(150,50),(200,50),(250,50),(300,50),(350,50),(400,50),(450,50)],]

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
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','','']]


# Variable si ya termino el juego
game_over = False

# Fps
clock = pygame.time.Clock()

# funcion llenar tablero con zombies y tumbas
def llenar_tablero_z(cantidad_z):
    for i in range(cantidad_z):
        num_aleatorio_x = random.randint(0, 7)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 'z'

llenar_tablero_z(1)

def llenar_tablero_t(cantidad_t):
    for i in range(cantidad_t):
        num_aleatorio_x = random.randint(0, 7)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 't'
        else:
            llenar_tablero_t(cantidad_t - i)

llenar_tablero_t(1)

def llenar_tablero_o(cantidad_o):
    for i in range(cantidad_o):
        num_aleatorio_x = random.randint(0, 7)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 'o'

llenar_tablero_o(3)

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
            
            # Graficar objetos
            if tablero[fil][col] == 'z':
                screen.blit(zombien, coordenadas[fil][col])
            elif tablero[fil][col] == 'zc':
                screen.blit(zombie_comido,coordenadas[fil][col])
            elif tablero[fil][col] == 't':
                screen.blit(tumban, coordenadas[fil][col])
            elif tablero[fil][col] == 'c':
                screen.blit(cerebro, coordenadas[fil][col])
            elif tablero[fil][col] == 'o':
                screen.blit(obstaculo, coordenadas[fil][col])

# Movimiento aleatorio zombies
def mover_zombies():
    for fil in range(8): 
        for col in range(10):
            if tablero[fil][col] == 'z':
                
                num_aleatorio = random.randint(0, 3)

                print('zombie en:', fil, col)
                if num_aleatorio == 0:
                    print('Movimiento: Arriba')
                elif num_aleatorio == 1:
                    print('Movimiento: Abajo')
                elif num_aleatorio == 2:
                    print('Movimiento: Izquierda')
                elif num_aleatorio == 3:
                    print('Movimiento: Derecha')

                if num_aleatorio == 0: #movimiento arriba
                    if fil - 1 >= 0 and tablero[fil-1][col] != 'z' and tablero[fil-1][col] != 't' and tablero[fil-1][col] != 'o': 
                        tablero[fil][col] = ''

                        if tablero[fil - 1][col] == 'c':
                            tablero[fil-1][col] == 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil - 1][col] = 'z'
                        

                elif num_aleatorio == 1: #movimiento abajo
                    if fil + 1 <= 7 and tablero[fil+1][col] != 'z' and tablero[fil+1][col] != 't' and tablero[fil+1][col] != 'o':
                        tablero[fil][col] = ''
                        
                        if tablero[fil + 1][col] == 'c':
                            tablero[fil + 1][col] == 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil + 1][col] = 'z'

                elif num_aleatorio == 2: #movimiento izquierda
                    if col - 1 >= 0 and tablero[fil][col-1] != 'z' and tablero[fil][col-1] != 't' and tablero[fil][col-1] != 'o':
                        tablero[fil][col] = ''

                        if tablero[fil][col-1] == 'c':
                            tablero == 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col - 1] = 'z'
                elif num_aleatorio == 3: #movimiento derecha
                    if col + 1 <= 9 and tablero[fil][col+1] != 'z' and tablero[fil][col+1] != 't' and tablero[fil][col+1] != 'o':
                        tablero[fil][col] = ''
                        
                        if tablero [fil][col+1] == 'c':
                            tablero[fil][col+1] == 'zc'
                            print('Zombie ha comido un cerebro')
                        else:
                            tablero[fil][col + 1] = 'z'

# def moviemiento_zombie_comido ():
                            
poner_cerebro = False
poner_obstaculo = False
borrar_objeto = False

# Agregar cerebro
def agregar_cerebro_obstaculos(x, y, tipo):
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

            elif x >= 300 and x <= 400 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Obstaculo]')

                if poner_obstaculo:
                    poner_obstaculo = False
                else:
                    poner_obstaculo = True
                    poner_cerebro = False
                    borrar_objeto = False

            elif x >= 225 and x <= 275 and y >= (0 + espacio_botones) and y <= (40 + espacio_botones):
                print('[Trash]')

                if borrar_objeto:
                    borrar_objeto = False
                else:
                    poner_cerebro = False
                    poner_obstaculo = False
                    borrar_objeto = True

            elif poner_cerebro and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                agregar_cerebro_obstaculos(y, x, 'c')
            elif poner_obstaculo and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                agregar_cerebro_obstaculos(y, x, 'o')

            elif borrar_objeto and y >= 100:
                x = (x) // 50
                y = (y - 100) // 50 
                tablero[y][x] = ''
            

            # Se le resta 100 por que no contamos el rango de los botones
            # Se mandan las coordenadas en orden inverso ya que el eje x y y estan al reves
            # en la matriz de coordenadas y en la matriz del tablero, por como se ven los pixeles 
            # y las matrices

    mover_zombies()

    graficar_objetos()
    

    # Graficar nuevos objetos (prueba)
    # screen.blit(background, (0, 0))
    # screen.blit(zombien, (0, 0))
    # screen.blit(tumban, (50, 50))
    # screen.blit(cerebro, (100, 100))

    # Actualizar pantalla
    pygame.display.update()


pygame.quit() #Cerrar el juego