import os, sys
import pygame
from pygame.locals import *

from settings import *

class Camera(object):
	"""
	Camera class for screen control
	"""
	def __init__(self, pos, mapSize, movementSpeed=1):
		if pos:
			self.x = pos[0]
			self.y = pos[1]
		
		self.mapSize = mapSize
		self.movementSpeed = movementSpeed
			
	def update(self, events):
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.move_camera(0, -1)
				elif event.key == pygame.K_DOWN:
					self.move_camera(0, 1)
				elif event.key == pygame.K_LEFT:
					self.move_camera(-1, 0)
				elif event.key == pygame.K_RIGHT:
					self.move_camera(1, 0)
					
	def move_camera(self, x, y):
		self.x += x * self.movementSpeed
		self.y += y * self.movementSpeed
		
		if self.x < 0 or self.mapSize[0] < RESOLUTION[0]:
			self.x = 0
		elif self.x + RESOLUTION[0] > self.mapSize[0]:
			self.x = self.mapSize[0] - RESOLUTION[0]
		
		if self.y < 0 or self.mapSize[1] < RESOLUTION[1]:
			self.y = 0
		elif self.y + RESOLUTION[1] > self.mapSize[1]:
			self.y = self.mapSize[1] - RESOLUTION[1]

		
		