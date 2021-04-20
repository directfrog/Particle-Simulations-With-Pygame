import pygame, sys
import random
from pygame.locals import *
clock = pygame.time.Clock()

pygame.init()
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

particles = []
for x in range(1000):
		rect = pygame.Rect(random.randint(0, screen_width-20), random.randint(0, screen_height-20), 10, 10)
		particles.append([rect, 0])

while True:
	screen.fill((0, 0, 0))
	
	for particle in particles:
		pygame.draw.rect(screen, (255, 255, 255), particle[0])
		particle_movement = 0
		
		if particle[0].y < screen_height-10:
			particle[1] += 1.3
		else:
			particle[1] = 0	

		particle_movement += particle[1]
		particle[0].y += particle_movement


	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()
	pygame.display.update()
	clock.tick(60)
