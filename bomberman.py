import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)

DIRT = 0
BLOCK = 1

colours = {
DIRT : BROWN,
BLOCK : BLACK
}

tilemap = [
[DIRT, DIRT, DIRT, DIRT, DIRT],
[DIRT, BLOCK, BLOCK, BLOCK, DIRT],
[DIRT, DIRT, DIRT, DIRT, DIRT]
]

TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

pygame.display.set_caption('BomberCat!')

while True:
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE,TILESIZE,TILESIZE))
    pygame.display.update()
