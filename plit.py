import pygame, sys
from pygame.locals import *

# constants
WIDTH  = 600
HEIGHT = 400

class Entity:
    """Parent class for anything that is 'living' (NPC, player, etc.)"""
    x    = 0 # entity's x coordinate
    y    = 0 # entity's y coordinate
    velx = 0 # entity's velocity in x direction
    vely = 0 # entity's velocity in y direction
    sprite = None # sprite to represent entity (null for invisible)
    
    def __init__(self, sprite):
        self.sprite = sprite
        
    def draw(self, surface):
        if self.sprite is not null:
            surface.blit(self.sprite, (self.x, self.y))

class Player(Entity):
    """The player's character. Can have more than one?"""
    pass
    
class NPC(Entity):
    """Non-player entity."""
    pass

class Tile:
    """Tile in the game world."""
    pass

class World:
    """Represents the (visible) game world. Holds all visible entities (and some hidden)"""
    players = []
    npcs = []
    tiles = []

def setup():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Plit')
    #DISPLAYSURF.blit()
    
    # player setup
    player = Player(None)

def update():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

setup()
update()