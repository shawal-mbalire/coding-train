import random
import pygame

width, height,length = 800, 800, 800

class Star:

    def __init__(self):
        self.x:float = random.randint(-width, width)
        self.y:float = random.randint(-height,height)
        self.z:float = random.randint(2,length)
        # self.z = length

    def update(self, speed):
        self.z = self.z - speed
        if self.z<1:
            self.z = length

    def show(self, screen):

        sx:float = map_range(self.x/self.z,-1,1,0,width)
        sy:float = map_range(self.y/self.z,-1,1,0,height)

        visibility = map_range(self.z,0,length,5,0)
        pygame.draw.circle(
            screen,
            'green',
            pygame.Vector2(sx,sy),
            visibility
        )
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min)*(out_max - out_min)//(in_max - in_min) + out_min
