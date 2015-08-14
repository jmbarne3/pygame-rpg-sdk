import os, sys
import pygame
from pygame.locals import *

from pygame.sprite import *

from lib.GameObjects import *

from settings import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class RPGMain:
	"""
	The Main RPG Class - This class handles the main
	initialization and creation of the game.
	"""
	def __init__(self):
		pygame.init()
		self.width = RESOLUTION[0]
		self.height = RESOLUTION[1]
		self.screen = pygame.display.set_mode((self.width,
												self.height))
		self.backgrounds = RenderPlain()
		self.sprites = RenderPlain()

	def MainLoop(self):
		bg = Background(self.screen.get_size(), (25, 50, 25), 'background.jpg')
		self.backgrounds.add(bg)
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				else:
					self.update()
					self.draw(self.screen)

	def update(self):
		self.backgrounds.update()
		self.sprites.update()

	def draw(self, surface):
		self.backgrounds.draw(surface)
		self.sprites.draw(surface)
		pygame.display.flip()

if __name__ == '__main__':
	MainWindow = RPGMain()
	MainWindow.MainLoop()