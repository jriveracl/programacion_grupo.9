import pygame,sys,random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 600)
background = pygame.image.load("assets/background.png").convert()
player1_widht = 15
player1_height = 90

player2_widht = 15
player2_heigt = 90

#coordenadas de los jugadores y sus velocidades
player1_x_coor = 50
player1_y_coor = 255
player1_y_speed = 0

player2_x_coor = 745
player2_y_coor = 255
player2_y_speed = 0

#coordenadas de la pelota y sus velocidades
pelota_x = 400
pelota_y = 300

pelota_speed_x = 3
pelota_speed_y = 3

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    
    screen.blit(background[0, 0])

    if pelota_x > 780 or pelota_x < 10:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x *= -1
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    player1 = pygame.draw.rect(screen, BLACK, (player1_x_coor,player1_y_coor, player1_widht, player1_height))
    player2 = pygame.draw.rect(screen, BLACK, (player2_x_coor,player2_y_coor, player2_widht, player2_heigt))
    pelota = pygame.draw.circle(screen, BLACK, (pelota_x, pelota_y), 10)

    pygame.display.flip()
    clock.tick(80)

pygame.quit()