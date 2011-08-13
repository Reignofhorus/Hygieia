#! /usr/bin/env python

class Human:
	""" The human menace """
	
	def __init__(self, Screen, Location, Space, Radius, Mass):
		""" Creates Pandora.  Right now Pandora is just a ball """
		self.Screen = Screen
		self.Location = Location
		self.Space = Space
		self.Radius = Radius
		self.Mass = Mass

	def AddPlayerToWorld(self):
		Inertia = pymunk.moment_for_circle(self.Mass, 0, self.Radius)
		self.Body = pymunk.Body(self.Mass, Inertia)
		self.Body.position = self.Location
		self.Character = pymunk.Circle(self.Body, self.Radius)
		
		self.Space.add(self.Body, self.Character)

	def DrawPlayer(self, pygame):
		LocConv = int(self.Character.body.position.x), 100-int(self.Character.body.position.y)
		pygame.draw.circle(self.Screen, (138, 184, 248), LocConv, int(self.Character.radius), 2)

class Virus:
	""" The Virus """