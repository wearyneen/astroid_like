from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    