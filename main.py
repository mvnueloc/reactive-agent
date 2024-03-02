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
background = pygame.image.load('static/background.png')
zombie = pygame.image.load('static/zombie1.png')
zombie_comido = pygame.image.load('static/zombie_comido.png')
tumba = pygame.image.load('static/tumba.png')
cerebro = pygame.image.load('static/cerebro.png')
obstaculo = pygame.image.load('static/obstaculo.png')

# Escalar imagenes
zombien = pygame.transform.scale(zombie, (50, 50))
zombie_comido =  pygame.transform.scale(zombie_comido,(50,50))
tumban = pygame.transform.scale(tumba, (60, 60))
cerebro = pygame.transform.scale(cerebro, (40, 40))
background = pygame.transform.scale(background, (500, 500))
obstaculo = pygame.transform.scale(obstaculo, (50, 50))

# Matriz con los pixeles de la imagen background
# Corregi matriz de coordenadas
coordenadas = [[(0,0),(50,0),(100,0),(150,0),(200,0),(250,0),(300,0),(350,0),(400,0),(450,0)],
               [(0,50),(50,50),(100,50),(150,50),(200,50),(250,50),(300,50),(350,50),(400,50),(450,50)],
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
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],
           ['','','','','','','','','',''],]



# Solo apareceran aqui los zombies que ya hayan comido un cerebro
# tablero_zombie_comido = [['','','','','','','','','',''],
#                          ['','','','','','','','','',''], 
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],
#                          ['','','','','','','','','',''],]

# Variable si ya termino el juego
game_over = False

# Fps por seguno
clock = pygame.time.Clock()

# funcion llenar tablero con zombies y tumbas
def llenar_tablero_z(cantidad_z):
    for i in range(cantidad_z):
        num_aleatorio_x = random.randint(0, 9)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 'z'

llenar_tablero_z(1)

def llenar_tablero_t(cantidad_t):
    for i in range(cantidad_t):
        num_aleatorio_x = random.randint(0, 9)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 't'
        else:
            llenar_tablero_t(cantidad_t - i)

llenar_tablero_t(3)

def llenar_tablero_o(cantidad_o):
    for i in range(cantidad_o):
        num_aleatorio_x = random.randint(0, 9)
        num_aleatorio_y = random.randint(0, 9)

        if tablero[num_aleatorio_x][num_aleatorio_y] == '':
            tablero[num_aleatorio_x][num_aleatorio_y] = 'o'

llenar_tablero_o(8)

# Funcion para graficar objetos
def graficar_objetos():
    screen.blit(background, (0, 0)) #Fondo

    for fil in range(10):
        for col in range(10):
            
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

# Agregar cerebro
def agregar_cerebro(x, y):
    if tablero[x][y] == '':
        tablero[x][y] = 'c'



# Movimiento aleatorio zombies
def mover_zombies():
    for fil in range(10): 
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
                    if fil + 1 <= 9 and tablero[fil+1][col] != 'z' and tablero[fil+1][col] != 't' and tablero[fil+1][col] != 'o':
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



                
# Loop de juego
while not game_over:
    clock.tick(1) #Siempre corra a 30 fps

    for event in pygame.event.get(): #Obtener eventos
        if event.type == pygame.QUIT: #Si el evento es cerrar la ventana
            game_over = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            y , x = event.pos
            x = x // 50
            y = y // 50
            print('Click en la posicion',x, y)
            agregar_cerebro(x, y)

    mover_zombies()

    graficar_objetos()
    

    # Graficar nuevos objetos (prueba)
    # screen.blit(background, (0, 0))
    # screen.blit(zombien, (0, 0))
    # screen.blit(tumban, (50, 50))
    # screen.blit(cerebro, (100, 100))

    # Actualizar pantalla
    pygame.display.update()


pygame.quit()
    


