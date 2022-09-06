# pygame.draw.rect(pantalla, color, (x,y, tam,tam))
# pygame.draw.line(pantalla, color, (horizontal, vertical, (x,y) grosor )
# pygame.draw.circle (pantalla, color (x,y), radio )

import pygame, sys, random
pygame.init()

size = (800,600)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#coordenadas iniciales
cord_x = random.randint(0,700)
cord_y = random.randint(0,500)

speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if cord_x > 730 or cord_x < 0:
        speed_x *= -1
    if cord_y > 500 or cord_y < 0:
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y

    screen.fill(WHITE)

    for i in range(100, 700, 100):
        pygame.draw.line(screen, GREEN, [0,100], [cord_x,cord_y], 5)
        pygame.draw.rect(screen ,BLACK, [cord_x, cord_y, 80,80] )
        pygame.draw.circle(screen, RED, (cord_x, cord_y), 30)

    pygame.display.flip()
    clock.tick(50)