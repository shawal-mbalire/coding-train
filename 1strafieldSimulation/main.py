import pygame
from star import Star

pygame.init()

width,height,length = 400,400,400

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
running = True

stars:list[Star] = list()
stars_length = 100

for i in range(stars_length):
    stars.append(Star())

def draw():

    screen.fill('purple')
    for star in stars:
        star.update()
        star.show(screen)

if __name__ == '__main__':
    while True: 
        draw()
        pygame.display.flip()
