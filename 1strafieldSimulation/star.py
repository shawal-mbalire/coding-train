import random
import pygame

width, height,length = 400, 400, 400
class Star:
    def __init__(self):
        self.x:float = random.randint(0, width)
        self.y:float = random.randint(0,height)
        self.z:float = random.randint(0,length)

    def update(self):
        pass
    def show(self, screen):
        pygame.draw.circle(
            screen,
            'red',
            pygame.Vector2(self.x,self.y),
            10
        )
