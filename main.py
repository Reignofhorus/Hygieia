#! /usr/bin/env python

import sys, random, os
import pygame
import world

def main():
	#Init some stuff
	random.seed()
	pygame.init()
	
	#Some variables
	Width = 1024
	Height = 768
	Running = True
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	
	#Create the screen to drawn on and the system clock
	Screen = pygame.display.set_mode((Width, Height))
	pygame.display.set_caption("Hygieia")
	Clock = pygame.time.Clock()
	
	while Running:							#Main loop
		for event in pygame.event.get():			#Event loop
			if event.type == pygame.QUIT:			#Click close or alt+f4, kill it
				Running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:	#Hit escape, kill it
					Running = False
		
		Screen.fill(WHITE)
		
		
		
		pygame.display.flip()
		Clock.tick(60)


if __name__ == '__main__':
	sys.exit(main())
