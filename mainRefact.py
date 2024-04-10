import pygame
import random

class GameObject:
    def __init__(self, image_path, position, size):
        self.image = pygame.image.load(image_path)
        self.position = position
    
    def draw(self, screen):
        screen.blit(self.image, self.position)

class Zombie(GameObject):
    def __init__(self, image_path, position):
        super().__init__(image_path, position)
        self.eaten = False  # Por defecto, un zombie no ha comido

    def move(self):
        # Implementar lógica de movimiento básico
        pass

class EatenZombie(Zombie):
    def __init__(self, position):
        super().__init__('static/zombie_comido.png', position)
        self.eaten = True

    # Métodos específicos para un zombie comido, por ejemplo, moverse hacia la tumba

class UneatenZombie(Zombie):
    def __init__(self, position):
        super().__init__('static/zombie1.png', position)

    # Métodos específicos para un zombie no comido


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.game_objects = []  # Lista para todos los objetos del juego
    
    def add_object(self, game_object):
        """Agrega un objeto al juego."""
        self.game_objects.append(game_object)

    def add_background(self, game_object):
        background = pygame.image.load(game_object)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill((0, 0, 0))  # Limpiar pantalla
            for obj in self.game_objects:
                obj.draw(self.screen)  # Dibuja cada objeto en la pantalla
            
            pygame.display.flip()  # Actualizar pantalla
            self.clock.tick(60)  # FPS
            
        pygame.quit()

# Clases GameObject, Zombie, EatenZombie, y UneatenZombie van aquí

if __name__ == "__main__":
    game = Game()
    # Ejemplo de cómo agregar zombies
    zombie = UneatenZombie((50, 50))
    game.add_object(zombie)
    # game.run()

game.run()