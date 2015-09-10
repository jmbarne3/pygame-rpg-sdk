import sys, os
import json
import math

import pygame
from pygame.locals import *
from pygame.sprite import Sprite

from lib.Camera import *

import xml.etree.ElementTree as ET

from settings import *

class Tile(Sprite):
	"""
	Class for drawing a single tile
	"""
	def __init__(self, tilesetPos, tilePos, tileset):
		Sprite.__init__(self)
		self.tilesetPos = tilesetPos
		self.tileset = tileset
		self.rect = pygame.Rect(tilesetPos[0],
			                    tilesetPos[1],
								tileset.tileWidth,
								tileset.tileHeight)
								
		self.tilePosX = tilePos[0]
		self.tilePosY = tilePos[1]
		self.x = self.tilePosX
		self.y = self.tilePosY
		
	
	def update(self, events, camera):
		self.x = self.tilePosX - camera.x
		self.y = self.tilePosY - camera.y
		
	def draw(self, surface):
		surface.blit(self.tileset.image,
			         (self.x, self.y),
					 self.rect)

class Layer(object):
	"""
	Class for storing a layer of tiles
	"""
	def __init__(self, layer, tileset):
		self.tilesWide = int(layer.attrib['width'])
		self.tilesHigh = int(layer.attrib['height'])
		self.tiles = []
		
		tiles = layer.find('data').findall('tile')
		
		for idx, tile in enumerate(tiles):
			tilesetPos = self.get_tileset_pos(tile.attrib['gid'], tileset)
			tilePos = self.get_tile_pos(idx, tileset)
			self.tiles.append(Tile(tilesetPos, tilePos, tileset))
	
	def get_tileset_pos(self, tileGid, tileset):
		gid = int(tileGid)
		y = math.floor(gid / tileset.tilesWide)
		x = gid - (y * tileset.tilesWide) - 1
		return (int(x) * tileset.tileWidth, int(y) * tileset.tileHeight)
		
	def get_tile_pos(self, idx, tileset):
		y = math.floor(idx / self.tilesWide)
		x = idx - y * self.tilesWide
		return (int(x) * tileset.tileWidth, int(y) * tileset.tileHeight)
	
	def draw(self, surface):
		for tile in self.tiles:
			tile.draw(surface)
			
	def update(self, events, camera):
		for tile in self.tiles:
			tile.update(events, camera)
			
class Tileset(object):
	"""
	Class for describing a tilesheet
	"""
	def __init__(self, tileset):
		self.tileWidth = int(tileset.attrib['tilewidth'])
		self.tileHeight = int(tileset.attrib['tileheight'])
		self.firstgid = int(tileset.attrib['firstgid'])
		image = tileset.find('image')
		self.width = int(image.attrib['width'])
		self.height = int(image.attrib['height'])
		self.tilesWide = self.width / self.tileWidth
		self.tilesHigh = self.height / self.tileHeight
		self.image, self.rect = self.load_tileset_image(image)
		
	def load_tileset_image(self, image):
		imagePath = image.attrib['source']
		imagePath = imagePath.split('/')[-1]
		retval = pygame.image.load(os.path.join(TILESET_PATH, imagePath))
		return retval, retval.get_rect()

class Map(object):
	"""
	Class for storing tile layers
	"""
	def __init__(self, mapData):
		self.layers = []
		self.offset = {
			'x': 0,
			'y': 0
		}
		if mapData:
			self.load_map_data(mapData)
		self.camera = Camera(
			(0,0), (self.mapSize['x'], self.mapSize['y']), 10)
			
	def load_map_data(self, mapData):
		try:
			tree = ET.parse(os.path.join(MAPDATA_PATH, mapData))
		except:
			raise 'Could not open map data file.'
		
		data = tree.getroot()
		self.tileSize = {
			'x': int(data.attrib['tilewidth']),
			'y': int(data.attrib['tileheight'])
		}
		self.mapSize = {
			'x': int(data.attrib['width']) * self.tileSize['x'],
			'y': int(data.attrib['height']) * self.tileSize['y']
		}
		self.tileset = Tileset(data.find('tileset'))
		
		for prop in data.iter('property'):
			if prop.attrib['name'] == 'name':
				self.name = prop.attrib['value']
			
		for layer in data.findall('layer'):
			self.layers.append(Layer(layer, self.tileset))
		
	def update(self, events):
		self.camera.update(events)
		for layer in self.layers:
			layer.update(events, self.camera)
		
	def draw(self, surface):
		for layer in self.layers:
			layer.draw(surface)