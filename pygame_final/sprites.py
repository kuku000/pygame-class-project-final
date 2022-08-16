import pygame
import time
import sys, os
from setting import *
import setting
from font import*
#from plot import *
import math

class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 255, 255))
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 遊戲開始後，定義角色所處的層
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites,self.game.player

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 2 * TILESIZE
        self.height = 2 * TILESIZE

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

        # 飢餓程度
        self.blood = 100

        #物品籃
        #self.item_beg = []

    def update(self):
        self.movement()


        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.animate()

        self.x_change = 0
        self.y_change = 0

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

    def collide_blocks(self, direction):  # 角色碰撞方式
        if direction == "x":
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        # 如果綜向移動時撞到物品，角色停下

        if direction == "y":
            hits = pygame.sprite.spritecollide(self,self.game.blocks,False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def animate(self):  # 定義角色移動時動畫
            # 定義角色 向下 移動時圖片動畫
        down_animation = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 0, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 0, self.width, self.height)]
        # 定義角色 向上 移動時圖片動畫
        up_animation = [self.game.character_spritesheet.get_sprite(0, 2 * TILESIZE, self.width, self.height),
                        self.game.character_spritesheet.get_sprite(2 * TILESIZE, 2 * TILESIZE, self.width,self.height),
                        self.game.character_spritesheet.get_sprite(4 * TILESIZE, 2 * TILESIZE, self.width,self.height),
                        self.game.character_spritesheet.get_sprite(6 * TILESIZE, 2 * TILESIZE, self.width,self.height)]
            # 定義角色 向左 移動時圖片動畫
        left_animation = [self.game.character_spritesheet.get_sprite(0, 4 * TILESIZE, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 4 * TILESIZE, self.width,self.height),
                            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 4 * TILESIZE, self.width,self.height),
                            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 4 * TILESIZE, self.width,self.height)]
        # 定義角色 向右 移動時圖片動畫
        right_animation = [self.game.character_spritesheet.get_sprite(0, 6 * TILESIZE, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 6 * TILESIZE, self.width,
                                                                          self.height),
                            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 6 * TILESIZE, self.width,
                                                                          self.height),
                            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 6 * TILESIZE, self.width,
                                                                          self.height)]
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
                self.image = self.game.character_spritesheet.get_sprite(0, 2 * TILE_SIZE, self.width, self.height)
            else:
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向左移動，則使角色圖片變為面向左邊的圖片包
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 4 * TILE_SIZE, self.width, self.height)
            else:
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向右移動，則使角色圖片變為面向右邊的圖片包
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 6 * TILE_SIZE, self.width, self.height)
            else:
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER

        self.groups = self.game.all_sprites ,self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)



        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    @classmethod
    def house(cls, game, x, y):
        house = cls(game, x, y)
        house.width = 160
        house.height = 160
        house.image = house.game.buliding_spritesheet.get_sprite(38, 25, house.width, house.height)
        house.rect = house.image.get_rect()
        house.rect.x = house.x
        house.rect.y = house.y
        return house

    @classmethod
    def river(cls, game, x, y):
        river = cls(game, x, y)
        river.width = 160
        river.height = 192
        river.image = river.game.buliding_spritesheet.get_sprite(225, 25, river.width, river.height)
        river.rect = river.image.get_rect()
        river.rect.x = river.x
        river.rect.y = river.y
        return river

    @classmethod
    def shop(cls, game, x, y):
        shop = cls(game, x, y)
        shop.width = 160
        shop.height = 160
        shop.image = shop.game.buliding_spritesheet.get_sprite(400 ,25, shop.width, shop.height)
        shop.rect = shop.image.get_rect()
        shop.rect.x = shop.x
        shop.rect.y = shop.y
        return shop

class Ground(pygame.sprite.Sprite):   # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # 讀取地板素材
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(WHITE)
        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    @classmethod
    def terrainA(cls, game, x, y):
        terrainA= cls(game, x, y)
        terrainA.width = TILE_SIZE
        terrainA.height = TILE_SIZE
        terrainA.image = terrainA.game.terrain_spritesheet.get_sprite(192, 192, terrainA.width, terrainA.height)
        return terrainA

    @classmethod
    def terrainB(cls, game, x, y):
        terrainB = cls(game, x, y)
        terrainB.width = TILE_SIZE
        terrainB.height = TILE_SIZE
        terrainB.image = terrainB.game.terrain_spritesheet.get_sprite(256, 192, terrainB.width,terrainB.height)
        return terrainB

    @classmethod
    def terrainC(cls, game, x, y):
        terrainC = cls(game, x, y)
        terrainC.width = TILE_SIZE
        terrainC.height = TILE_SIZE
        terrainC.image = terrainC.game.terrain_spritesheet.get_sprite(128, 192, terrainC.width, terrainC.height)
        return terrainC

    @classmethod
    def modA(cls, game, x, y):
        modA = cls(game, x, y)
        modA.width = TILE_SIZE
        modA.height = TILE_SIZE
        modA.image = modA.game.terrain_spritesheet.get_sprite(0, 232, modA.width, modA.height)
        return modA

    @classmethod
    def modB(cls, game, x, y):
        modB = cls(game, x, y)
        modB.width = TILE_SIZE
        modB.height = TILE_SIZE
        modB.image = modB.game.terrain_spritesheet.get_sprite(32, 232, modB.width, modB.height)
        return modB

    @classmethod
    def rockB(cls, game, x, y):
        rockB = cls(game, x, y)
        rockB.width = TILE_SIZE
        rockB.height = TILE_SIZE
        rockB.image = rockB.game.terrain_spritesheet.get_sprite(32, 160, rockB.width, rockB.height)
        return rockB

    @classmethod
    def road(cls, game, x, y):
        road = cls(game, x, y)
        road.width = TILE_SIZE
        road.height = TILE_SIZE
        road.image = road.game.terrain_spritesheet.get_sprite(0, 232, road.width, road.height)
        return road

    def update(self):
        pass

class NPC(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.NPCS
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.name = None
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2*TILE_SIZE
        self.height = 2*TILE_SIZE
        #初始化NPC圖案(色塊)
        self.image =pygame.Surface([self.width,self.height])
        self.image.fill(RED)
        # 設置 NPC 路徑
        self.path = None
        self.path_pos = 0
        # 設置 NPC 面向
        self.facing = 'down'
        self.animation_loop = 1
        # 設置 NPC 移動
        self.moving = False
        self.x_change = 0
        self.y_change = 0
        self.speed = 6
        self.max_count = TILE_SIZE / self.speed
        self.move_count = 0
        self.move_goal_x = None
        self.move_goal_y = None

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):  # NPC移動
        if self.moving:
            if self.rect.x == self.move_goal_x and self.rect.y == self.move_goal_y:
                self.moving = False
                self.x_change = 0
                self.y_change = 0
            else:
                if self.path[self.path_pos] == 'x+':
                    self.x_change += self.speed
                elif self.path[self.path_pos] == 'x-':
                    self.x_change -= self.speed

                if self.path[self.path_pos] == 'y+':
                    self.y_change += self.speed
                elif self.path[self.path_pos] == 'y-':
                    self.y_change -= self.speed

        self.path_pos +=1

        if self.x_change == 0:
            if self.y_change > 0:
                self.facing = 'down'
            elif self.y_change < 0:
                self.facing = 'up'

        if self.y_change == 0:
            if self.x_change > 0:
                self.facing = 'right'
            elif self.y_change < 0:
                self.x_change = 'left'

    def animate(self):
        pass

    #長老
    @classmethod
    def king(cls,game,x,y):
        king =cls(game,x,y)
        king.name = 'posiyn'
        king.moving = False
        king.path = KING_PATH
        king.speed = 1

        king.width = 2*TILESIZE
        king.height = 2*TILESIZE
        
        king.facing = 'down'

    @classmethod
    def river_man(cls,game,x,y):
        river_man = cls(game, x, y)
        river_man.name = 'Watan'
        #river_man.path = KING_PATH
        #river_man.speed = 1

        river_man.width = 2 * TILESIZE
        river_man.height = 2 * TILESIZE

        river_man.facing = 'down'
    @classmethod
    def house_man(cls,game,x,y):
        house_man = cls(game, x, y)
        house_man.name = 'Losin'
        #house_man.path = KING_PATH
        #house_man.speed = 1

        house_man.width = 2 * TILESIZE
        house_man.height = 2 * TILESIZE

        house_man.facing = 'down'

    def move_detection(self):
        pass













