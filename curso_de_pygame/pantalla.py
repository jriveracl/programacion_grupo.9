import pygame, sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    
    screen.fill(WHITE)

    for i in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, [i,300, i,50])
        pygame.draw.line(screen, BLACK, [i,0], [0,100], 5)

    pygame.draw.rect(screen, GREEN, [100,400, 10,200], 5)
    pygame.draw.line(screen, BLACK, [100,200], [100,300], 10)

    pygame.display.flip()

    clock.tick(60)