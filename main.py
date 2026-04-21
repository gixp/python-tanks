import pygame
from level import Level


class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption('Tanks v5')   
		self.screen_size = pygame.display.get_surface().get_size()
		self.clock = pygame.time.Clock()
        
		self.level = Level()

	def run(self):     
		while True:
			self.stop()

			self.screen.fill((0, 0, 0))
			self.level.run()

			pygame.display.update()		
			self.clock.tick(60)	

	def stop(self):
		for event in pygame.event.get():                                   
			if event.type == pygame.QUIT:									
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()	


if __name__ == '__main__':
	game = Game()
	game.run()