#!/usr/bin/python3.4

import sys, pygame
from pygame.locals import *

class Screen:

    screen_x = 0
    screen_y = 0

    screen = None

    def start_screen(self, x ,y ,title):
        self.screen_x = x
        self.screen_y = y
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        pygame.display.set_caption(title)




    def change_background_color(self,red,green,blue):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((red,green,blue))
        self.screen.blit(background,(0,0))
        pygame.display.flip()