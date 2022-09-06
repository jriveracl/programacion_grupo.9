
import pygame, random

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		pygame.mouse.set_visible(0)

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		player.rect.x = mouse_pos[0]
		player.rect.y = 510

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/laser.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	
	def update(self):
		self.rect.y -= 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background = pygame.image.load("assets/fondo_de_batalla.jpg")

pygame.init()
screen = pygame.display.set_mode([1300,600])
clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(80):
	meteor = Meteor()
	meteor.rect.x = random.randrange(1300)
	meteor.rect.y = random.randrange(450)

	meteor_list.add(meteor)
	all_sprite_list.add(meteor)

sound = pygame.mixer.Sound("laser5.wav")

player = Player()
all_sprite_list.add(player)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			laser = Laser()
			laser.rect.x = player.rect.x + 45
			laser.rect.y = player.rect.y - 20

			all_sprite_list.add(laser)
			laser_list.add(laser)
			sound.play()

	all_sprite_list.update() 
	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)

		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			score += 1
		
		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
 
	screen.blit(background, [0,0])
	all_sprite_list.draw(screen)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
