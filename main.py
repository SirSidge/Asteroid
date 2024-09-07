import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	AsteroidField()

	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		
		screen.fill((0, 0, 0))
		for obj in updatable:
			obj.update(dt)
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
