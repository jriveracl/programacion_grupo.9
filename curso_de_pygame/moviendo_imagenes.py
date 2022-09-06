import pygame, sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

x_coor = 10
y_coor = 10

x_speed = 0
y_speed = 0

size = (900, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys,exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            
    screen.fill(WHITE)

    x_coor += x_speed
    y_coor += y_speed
    
    pygame.draw.rect(screen, BLACK, (x_coor,y_coor, 100,100))
    pygame.display.flip()
    clock.tick(60)

pygame.quit
