import pygame
from setting import *
from tile_element import Tile_Element


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite


# Tile_element 各自類型
class TerrainA(Tile_Element):
    clip_x = 192
    clip_y = 192
    layer = 1
    tile_type = 'terrain'


class TerrainB(Tile_Element):
    clip_x = 256
    clip_y = 192
    layer = 1
    tile_type = 'terrain'


class TerrainC(Tile_Element):
    clip_x = 128
    clip_y = 192
    layer = 1
    tile_type = 'terrain'


class Road(Tile_Element):
    clip_x = 0
    clip_y = 32
    layer = 1
    tile_type = 'terrain'


class Block(Tile_Element):
    clip_x = 0
    clip_y = 288
    layer = 2
    tile_type = 'block'