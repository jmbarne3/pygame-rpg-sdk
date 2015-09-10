import os, sys
import pygame
from pygame.locals import *

from pygame.sprite import *

from lib.Controls import *
from lib.GameObjects import *
from lib.BaseGameScreens import *
from lib.GameScreens.StartScreen import *
from lib.GameScreens.MapScreen import *

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
		pygame.key.set_repeat(40, 40)
		self.width = RESOLUTION[0]
		self.height = RESOLUTION[1]
		self.screen = pygame.display.set_mode((self.width,
												self.height))
		self.GameScreen = MapScreen('debug.tmx')


	def MainLoop(self):
		while 1:
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.QUIT:
					sys.exit()

				self.update(events)
				self.draw(self.screen)

	def update(self, events):
		self.GameScreen.update(events)

	def draw(self, surface):
		self.GameScreen.draw(surface)
		pygame.display.flip()

if __name__ == '__main__':
	MainWindow = RPGMain()
	MainWindow.MainLoop()