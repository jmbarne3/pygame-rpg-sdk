import os, sys
import pygame
from pygame.locals import *

import settings

from pygame.sprite import *

from lib.GameObjects import *
from lib.BaseGameScreens import *
from lib.Camera import *
from lib.Controls import *
from lib.TileMap import *

class MapScreen(GameScreen):
	def __init__(self, initial_map):
		GameScreen.__init__(self)
		if initial_map:
			self.load_map(initial_map)
		else:
			self.current_map = None
			
	def load_map(self, initial_map):
		camera = Camera
		self.current_map = Map(initial_map)
		
	def update(self, events):
		self.current_map.update(events)
		
	def draw(self, surface):
		self.current_map.draw(surface)
	 