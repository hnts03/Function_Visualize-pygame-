import pygame, sys
from pygame.locals import *

pygame.init()                                   # pygame.init()                             :: initializing
dispsurf = pygame.display.set_mode((440,300))   # pygame.display.set_mode((x_size, y_size)) :: make window x_size * y_size
                                                #                                              return pygame.Surface object
pygame.display.set_caption('hello world!')      # pygame.display.set_caption                :: set window caption
while (True):
    for event in pygame.event.get():            # pygame.event.get()                        :: get event(checking  new event) from pygame
        if event.type == QUIT:
            pygame.quit()                       # quit pygame
            sys.exit()                          # quit while loop
        pygame.display.update()                 # Draw game state on window