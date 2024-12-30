# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


#main function
def main():
    #initalise pygame
    pygame.init()
    print("Starting asteroids!")
    #Print out the SCREEN_WIDTH and SCREEN_HEIGHT values when main.py is run. Use the following format:
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #create gui window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #initiate game loop
    while True:
        screen.fill('black')
        pygame.display.flip()
    

#ensure only runs if file is run
if __name__ == "__main__":
    main()