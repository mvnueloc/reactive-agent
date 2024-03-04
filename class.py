import pygame as pg
import random

class Game():
    """
    A class representing reactive agents simulation.
    """
    __rows = 10
    __cols = 10
    __game_over = False
    __agents = []

    def __init__(self, screen: pg.Surface) -> None:
        self.__screen = screen
        self.__clock = pg.time.Clock()
        self.initComponents()

    def initComponents(self) -> None:
        self.__background = pg.transform.scale(pg.image.load("static/background.png"), (500, 500))

        self.__coords = [[(i * 50, j * 50) for i in range(self.__cols)] for j in range(self.__rows)]
        self.__table = [['' for _ in range(self.__cols)] for _ in range(self.__rows)]

        self.__obstacleIcon = pg.transform.scale(pg.image.load("static/obstaculo.png"), (50, 50))
        self.__agentIcon = pg.transform.scale(pg.image.load("static/zombie1.png"), (50, 50))
        self.__baseIcon = pg.transform.scale(pg.image.load("static/tumba.png"), (60, 60))

        self.__screen.blit(self.__background, (0, 0))

        firstAgent = Agent("Agent 1", self.__agentIcon, self.__table, self.__screen)
        secondAgent = Agent("Agent 2", self.__agentIcon, self.__table, self.__screen)

        self.__agents.append(firstAgent)
        self.__agents.append(secondAgent)

    def moveAgents(self):
        for agent in self.__agents:
            agent.updatePosition()

    #erase this method, it's only for debugging
    # def printTable(self):
    #     for row in self.__table:
    #         print(row)
    
    # #erase this method, it's only for debugging
    # def printCoords(self):
    #     for row in self.__coords:
    #         print(row)

    #run method
    def run(self):
        while not self.__game_over:
            self.__clock.tick(5)
            
            for event in pg.event.get():    
                if event.type == pg.QUIT:
                    self.__game_over = True
            
            self.__screen.blit(self.__background, (0, 0))
            self.moveAgents()
            self.printTable()

            pg.display.update()
        
class Agent():

    def __init__(self, name: str, agentIcon: pg.surface, table: list[list], screen: pg.surface) -> None:
        self.__name = name
        self.__agentIcon = agentIcon
        self.__table = table
        self.__hasItem = False
        self.__screen = screen

        #random position
        self.__x = random.randint(0, len(table[0]) - 1)
        self.__y = random.randint(0, len(table) - 1)

        #place agent in the screen
        self.__screen.blit(self.__agentIcon, (self.__x * 50, self.__y * 50))
        self.__table[self.__y][self.__x] = 'A'

    def moveRandom(self) -> None:
        while True:
            direction = random.randint(0, 3)

            if direction == 0 and self.__x:
                self.__x -= 1
                return
            elif direction == 1 and self.__x < len(self.__table[0]) - 1:
                self.__x += 1
                return
            elif direction == 2 and self.__y:
                self.__y -= 1
                return
            elif direction == 3 and self.__y < len(self.__table) - 1:
                self.__y += 1
                return
                

    def updatePosition(self):
        self.moveRandom()
        self.__screen.blit(self.__agentIcon, (self.__x * 50, self.__y * 50))


        

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((500, 500))
    pg.display.set_caption("Reactive Agents")
    
    game = Game(screen)
    game.run()