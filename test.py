import pygame
from pygame.locals import *
import sys
from random import randint

screen = pygame.display.set_mode((1024,768),0,32)

pygame.init()
while 1:
	for event in pygame.event.get():
	    if event.type==QUIT:
	        exit()

	x,y = pygame.mouse.get_pos()
	r = 0.1

	if pygame.mouse.get_pressed()[0]:
	    r+=0.1
	    pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255),(x,y),r))

	pygame.display.update()
