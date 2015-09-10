import os, sys
import pygame
from pygame.locals import *

import settings

from pygame.sprite import *

from lib.GameObjects import *
from lib.BaseGameScreens import *
from lib.Controls import *

class StartScreen(GameScreen):
	def __init__(self):
		GameScreen.__init__(self)
		self.backgrounds.add(Background(settings.RESOLUTION, (25, 50, 25), 'background.jpg'))
		self.controls.add(Label("lbl_main", "Hello World", 36, (255,255,255), (400, 50), None))
		lb = LinkButton("lb_newGame", "New Game", 36, (255,255,255), (400, 95), None)
		lb.on_enter = self.lb_on_enter
		lb2 = LinkButton("lb_exit", "Exit", 36, (255,255,255), (400, 130), None)
		lb2.on_enter = self.lb2_on_enter
		self.controls.add(lb)
		self.controls.add(lb2)

	def update(self, events):
		GameScreen.update(self, events)

	def draw(self, surface):
		GameScreen.draw(self, surface)

	def lb_on_enter(self):
		print "Starting new game..."

	def lb2_on_enter(self):
		print "Exiting game..."
		sys.exit()