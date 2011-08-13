#! /usr/bin/env python

import random
import pygame

class World:
	""" The world that Pandora lives in.  """
	
	COLORMASK = (255,0,210, 255)
	cBrazil = (255, 255, 0)
	cUruguay = (28, 220, 82)
	cArgentina = (17, 0, 0)
	cParaguay = (0, 255, 255)
	cBolivia = (255,30,146)
	Regions = []
	
	def __init__(self, Screen):
		""" Creates the world """
		self.Screen = Screen
		
		#Load background map
		self.BG = pygame.image.load("testmap.png")
		self.BG.set_colorkey(self.COLORMASK)
		
		self.CreateRegions()

	def CreateRegions(self):
		random.seed()
		
		#Pick a random point to begin with
		Point = [random.randint(0, self.BG.get_width()), random.randint(0, self.BG.get_height())]
		print "Initial point:", Point
		
		#edge of map
		if(Point[0] == 0 or Point[0] == self.BG.get_width() or Point[1] == 0 or Point[1] == self.BG.get_height()):
			print "out of bounds"
			return
		
		NewColor = self.BG.get_at(Point)
		
		if (NewColor == self.COLORMASK):
			print "in water"
			return
		
		NewRegion = Region("Brazil", 1000)
		NewRegion.Color = NewColor
		print "Color at point:", NewRegion.Color
		
		SameColor = True
		
		while SameColor:
			Point[1] += 1
			print "New point:", Point
			
			NewColor = self.BG.get_at(Point)
			print "New color:", NewColor
			
			if NewColor != NewRegion.Color:
				print "different color"
				SameColor = False
		
		self.Regions.append(NewRegion)

	def DrawMap(self):
		self.Screen.blit(self.BG, (0,0))

class Region:
	""" A region on the map """
	
	Name = None		#Name of the region
	Population = []		#Population of region, array of type Human
	Color = None
	Boundaries = []

	def __init__(self, vName, vPopulation):
		Name = vName
		Population = vPopulation
