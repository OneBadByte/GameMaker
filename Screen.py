#!/usr/bin/python3.4

import sys, pygame

class Screen:

    screen_x = 0
    screen_y = 0

    screen = None

    def __init__(self):
        pygame.init()


    def set_screen_height_and_width(self, x=0, y=0):
        self.screen_x = x
        self.screen_y = y
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))


    def start_screen(self, title="testing"):
        pygame.display.set_caption(title)

    def change_background_color(self,red,blue,green):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((red,blue,green))
        self.screen.blit(background,(0,0))
        pygame.display.flip()

