import sys,pygame
class Entity:


    white =(250,250,250)
    magenta =(250, 50, 250)


    def __init__(self, name, screen, width, height, x , y):
        self.name = name
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(x,y,width,height)
        pygame.draw.rect(screen ,self.magenta, self.rect)
        #pygame.display.update(self.rect)


    def move_rect(self,screen, x, y):
        #print(self.rect.move(x,y))
        pygame.draw.rect(screen, self.magenta, self.rect.move(x,y))
        #pygame.display.update()





