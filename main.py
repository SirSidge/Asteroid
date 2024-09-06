import pygame, constants
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		screen.fill((0, 0, 0))
		pygame.display.flip()
		dt = clock.tick(60) / 1000
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	pass

if __name__ == "__main__":
	main()
