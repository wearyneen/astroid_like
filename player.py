import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draw the player's triangle
    def draw(self, screen):
        player_icon = pygame.draw.polygon(screen, 'white', self.triangle(), width=2)
        return player_icon