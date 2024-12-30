# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


#main function
def main():
    #initalise pygame
    pygame.init()
    #create gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #restrict fps
    clock = pygame.time.Clock()
    dt = 0
    #initiate game loop
    while True:
        #enable X button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        pygame.display.flip()

        #fps restriction
        delta_time = clock.tick(60)
        dt = delta_time / 1000
    

#ensure only runs if file is run
if __name__ == "__main__":
    main()