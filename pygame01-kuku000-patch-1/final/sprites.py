# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 22:22:27 2022

@author: win10
"""
import pygame
import time
import sys, os
from config import *

from font import*
from plot import *
import math
#import pygame.sprite
from tile_element import Tile_Element

class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 255, 255))
        return sprite



class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
     # 遊戲開始後，定義角色所處的層
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE


        self.animation_loop = 1
        # 定義角色初始移動變量
        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'

        # 定義角色初始移動變量
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        # 獲取角色位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def movement(self):
        # 操控上下左右
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'

    def collide_blocks(self, direction):    # 角色碰撞方式
        # 如果撞到被定義為 block 的物件
        for block in self.game.blocks.blocks_list:
            hit = self.rect.colliderect(block.rect)
            # 如果橫向移動時撞到物品，角色停下
            if direction == "x":
                if hit:
                    if self.x_change > 0:
                        self.rect.right = block.rect.left
                    if self.x_change < 0:
                        self.rect.left = block.rect.right
            # 如果綜向移動時撞到物品，角色停下
            if direction == "y":
                if hit:
                    if self.y_change > 0:
                        self.rect.bottom = block.rect.top
                    if self.y_change < 0:
                        self.rect.top = block.rect.bottom

    def animate(self):  # 定義角色移動時動畫
        # 定義角色 向下 移動時圖片動畫
        down_animation = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 0, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 0, self.width, self.height)]
        # 定義角色 向上 移動時圖片動畫
        up_animation = [self.game.character_spritesheet.get_sprite(0, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 2*TILE_SIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 2*TILE_SIZE, self.width, self.height)]
        # 定義角色 向左 移動時圖片動畫
        left_animation = [self.game.character_spritesheet.get_sprite(0, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 4*TILE_SIZE, self.width, self.height),
                          self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 4*TILE_SIZE, self.width, self.height)]
        # 定義角色 向右 移動時圖片動畫
        right_animation = [self.game.character_spritesheet.get_sprite(0, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(2*TILE_SIZE, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(4*TILE_SIZE, 6*TILE_SIZE, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(6*TILE_SIZE, 6*TILE_SIZE, self.width, self.height)]
        # 如果角色是向下移動，則使角色圖片變為面向下的圖片包
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向上移動，則使角色圖片變為面向上的圖片包
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 2*TILE_SIZE, self.width, self.height)
            else:
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向左移動，則使角色圖片變為面向左邊的圖片包
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 4*TILE_SIZE, self.width, self.height)
            else:
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向右移動，則使角色圖片變為面向右邊的圖片包
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 6*TILE_SIZE, self.width, self.height)
            else:
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1








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

class ModA(Tile_Element):
    clip_x = 0
    clip_y = 232
    layer = 1
    tile_type = 'terrain'
class ModB(Tile_Element):
    clip_x = 32
    clip_y = 232
    layer = 1
    tile_type = 'terrain'

class RockB(Tile_Element):
    clip_x = 32
    clip_y = 160
    layer = 1
    tile_type = 'terrain'


class Road(Tile_Element):
    clip_x = 0
    clip_y = 32
    layer = 1
    tile_type = 'terrain'


class House(Tile_Element):
    clip_x = 25
    clip_y = 25
    layer = 2
    width = 175
    height = 175

    tile_type = 'building'

class River(Tile_Element):
    clip_x = 225
    clip_y = 25
    layer = 2
    width = 175
    height = 175
    tile_type = 'building'

class Shop(Tile_Element):
    clip_x = 400
    clip_y = 25
    layer = 2
    width = 175
    height = 175
    tile_type = 'building'





