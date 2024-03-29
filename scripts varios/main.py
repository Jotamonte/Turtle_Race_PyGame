import pygame
import sys

class Game():

    corredores = []

    def __init__(self):

        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("backG.png") #le asignamos la varia

        self.runner = pygame.image.load("c1.png")




    def competir(self):

        x = 0
        hayGanador = False

        while True:
            # comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Refrescar, renderizar la pantalla
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()

            x += 2
            if x >= 700:
                hayGanador = True
                pygame.quit()
                sys.exit()
        
        

if __name__ == '__main__':

    pygame.init()
    game = Game()
    game.competir()
