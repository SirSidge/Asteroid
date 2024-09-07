import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		
		screen.fill((0, 0, 0))
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
#print("Starting asteroids!")
#print(f"Screen width: {constants.SCREEN_WIDTH}")
#print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
