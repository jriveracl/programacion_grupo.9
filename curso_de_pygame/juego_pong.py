import pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800,600)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player1_widht = 10
player1_height = 90

player2_widht = 10
player2_height = 90

#coordenadas de los jugadores
player1_x_coord = 50
player1_y_coord = 255
player1_y_speed = 0

player2_x_coord = 750
player2_y_coord = 255
player2_y_speed = 0

#coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

background = pygame.image.load("assets/fondo_de_pantalla.jpg").convert()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            if event.key == pygame.K_UP:
                player2_y_speed = -3 
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            if event.key == pygame.K_UP:
                player2_y_speed = 0 
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
    
    # limitando el recorrido de la pelota
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300

        pelota_speed_x *= -1
        pelota_speed_y *= -1

    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    # dar movimiento a los jugadores
    player1_y_coord += player1_y_speed
    player2_y_coord += player2_y_speed

    # moviendo la pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    screen.blit(background, [0, 0])

    player1 = pygame.draw.rect(screen, white, [player1_x_coord,player1_y_coord, player1_widht,player1_height])
    player2 = pygame.draw.rect(screen, white, [player2_x_coord,player2_y_coord, player2_widht,player2_height])
    pelota = pygame.draw.circle(screen, white, (pelota_x , pelota_y), 10)

    if pelota.colliderect(player1) or pelota.colliderect(player2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()