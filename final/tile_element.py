import pygame
from config import *
from sprites import *
import math


class Tile_Element(pygame.sprite.Sprite):
    """
    繼承用類別 clip_x clip_y  從圖片集切圖的原點座標
    layer 為
    """
    clip_x = 0
    clip_y = 0
    layer = 1
    tile_type = ''
    width = TILESIZE
    height = TILESIZE
    groups = None
    # 初始化用
    def __init__(self, game, x, y):
        self.game = game
        self._layer = self.layer
        self.set_groups(self.tile_type)

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE


        self.get_sprite(self.tile_type)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # 依照元素類型選擇圖片集並切圖片
    def get_sprite(self, tile_type):
        if tile_type == 'block':
            self.image = self.game.block_spritesheet.get_sprite(self.clip_x, self.clip_y, TILESIZE, TILESIZE)
        elif tile_type == 'terrain':
            self.image = self.game.terrain_spritesheet.get_sprite(self.clip_x, self.clip_y,  TILESIZE, TILESIZE)
        elif tile_type == "building":
            self.image = self.game.buliding_spritesheet.get_sprite(self.clip_x, self.clip_y,  int(self.width), int(self.height))

    # 依照元速類型選擇元素群組
    def set_groups(self, tile_type):
        if tile_type == 'block' or 'building':
            self.groups =  self.game.all_sprites,self.game.blocks
        elif tile_type == 'terrain':
            self.groups =  self.game.all_sprites,self.game.terrains
