import os, sys
import pygame
from pygame.locals import *

from pygame.sprite import *

from GameObjects import *
from Controls import *

class GameScreen:
	def __init__(self):
		self.backgrounds = RenderPlain()
		self.controls = Controls()
		self.sprites = RenderPlain()

	def update(self, events):
		self.backgrounds.update(events)
		self.controls.update(events)
		self.sprites.update(events)

	def draw(self, surface):
		self.backgrounds.draw(surface)
		self.sprites.draw(surface)
		self.controls.draw(surface)