import os, sys
import pygame
from pygame.locals import *

from pygame.sprite import *

class Control:
	def __init__(self, name, tabIndex=0):
		self.name = name
		self.tabIndex = tabIndex
		self.Selectable = False
		self.isSelected = False
		self.isActive = True

	def update(self):
		pass

	def draw(self, surface):
		pass

class Controls:
	def __init__(self, controls={}):
		self.controls = controls
		self.selectableControls = {}
		self.current_index = 0
	

	def update(self, events):
		self.selectableControls[self.current_index].isSelected = True;
		for event in events:
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.previous_control()
				elif event.key == pygame.K_DOWN:
					self.next_control()

		for name, control in self.controls.iteritems():
			control.update(events)

	def next_control(self):
		self.selectableControls[self.current_index].isSelected = False
		if self.current_index is not len(self.selectableControls) - 1:
			self.current_index = self.current_index + 1
		else:
			self.current_index = 0
		self.selectableControls[self.current_index].isSelected = True

	def previous_control(self):
		self.selectableControls[self.current_index].isSelected = False
		if self.current_index is not 0:
			self.current_index = self.current_index - 1
		else:
			self.current_index = len(self.selectableControls) - 1
		self.selectableControls[self.current_index].isSelected = True

	def draw(self, surface):
		for name, control in self.controls.iteritems():
			control.draw(surface)

	def add(self, control):
		self.controls[len(self.controls)] = control

		if control.Selectable:
			self.selectableControls[len(self.selectableControls)] = self.controls[len(self.controls) - 1]

	def remove(self, controlName):
		for idx, control in self.controls.iteritems():
			if control.name == controlName:
				del self.controls[idx]

class Label(Control):
	def __init__(self, name, text, fontSize=36, fontColor=(255,255,255), position=(0,0), font=None):
		Control.__init__(self, name)
		self.text = text
		self.fontColor = fontColor
		self.position = position
		self.font = pygame.font.Font(font, fontSize)
	
	def update(self, events):
		pass

	def draw(self, surface):
		text = self.font.render(self.text, 1, self.fontColor)
		surface.blit(text, self.position)

class LinkButton(Control):
	def __init__(self, name, text, fontSize=36, fontColor=(255, 255, 255), position=(0,0), font=None):
		Control.__init__(self, name)
		self.Selectable = True
		self.text = text
		self.fontColor = fontColor
		self.selectedFontColor = (120, 120, 200)
		self.position = position
		self.font = pygame.font.Font(font, fontSize)
		self.on_enter = self.on_enter

	def update(self, events):
		if self.isSelected:
			for event in events:
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_RETURN:
						self.on_enter()

	def draw(self, surface):
		if self.isSelected:
			text = self.font.render(self.text, 1, self.selectedFontColor)
		else:
			text = self.font.render(self.text, 1, self.fontColor)
		surface.blit(text, self.position)

	def on_enter(self):
		print "Enter has been pressed..."