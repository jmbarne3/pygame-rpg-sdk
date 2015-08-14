import os, sys
import pygame
from pygame.locals import *

from pygame.sprite import Sprite

from settings import *

class Background(Sprite):
	def __init__(self, size=(0,0), color=None, image=None):
		Sprite.__init__(self)
		if color is None and image is None:
			raise SystemExit, "You must provide a color or background image to Background"
		
		self.color = color
		if image is not None:
			self.image, self.rect = self.load_image(image)
		else:
			self.image = pygame.Surface(size).convert()
			self.image.fill(self.color)
			self.rect = self.image.get_rect()

	def load_image(self, image, colorkey=None):
		fullname = os.path.join(BACKGROUND_PATH, image)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image: ', name
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image, image.get_rect()

	def update(self):
		pass

class Character(Sprite):
	"""
	Main Character class that all PCs and NPCs will derive from.
	"""
	def __init__(self, name, image, position=(0,0)):
		Sprite.__init__(self)
		self.name = name
		self.image, self.rect = self.load_image(image, -1)
		self.position = position

	def load_image(self, image, colorkey=None):
		fullname = os.path.join(SPRITE_PATH, image)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image: ', name
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image, image.get_rect()

	def update(self):
		super(Sprite, self).update()

	def alive(self):
		return super(Sprite, self).alive()

class NonPlayableCharacter(Character):
	"""
	Non Playable Character class.
	"""
	def __init__(self, name, image, position=(0,0)):
		super(Character, self).__init__(name, image, position)

	def update(self):
		pass

	def alive(self):
		return super(NonPlayableCharacter, self).alive()

class PlayableCharacter(Character):
	"""
	Playable Character
	"""
	def __init__(self, name, image, position=(0,0)):
		Character.__init__(self, name, image, position)

	def update(self):
		pass

	def alive(self):
		return super(PlayableCharacter, self).alive()