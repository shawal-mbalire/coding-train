import pygame
from star import Star, map_range

pygame.init()

width,height,length = 800,800,800

screen = pygame.display.set_mode(
    size = (width,height),
)
clock = pygame.time.Clock()
running = True

stars:list[Star] = list()
stars_length = 1000

for i in range(stars_length):
    stars.append(Star())

def draw():

    screen.fill('black')
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x,mouse_y)
    speed = map_range(mouse_x,0,width,2,20)

    for star in stars:
        star.show(screen)
        star.update(speed)

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            pass
        draw()
        pygame.display.flip()
        clock.tick(20)
