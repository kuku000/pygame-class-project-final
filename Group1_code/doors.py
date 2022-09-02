import pygame
from setting import *


class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # 讀取地板素材
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((WHITE))
        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass

    @classmethod
    def house(cls, game, x, y):
        house = cls(game, x, y)
        house.width = TILE_SIZE
        house.height = TILE_SIZE
        house.image = house.game.terrain_spritesheet.get_sprite(192, 192, house.width, house.height)
        return house

    @classmethod
    def river(cls, game, x, y):
        river = cls(game, x, y)
        river.width = TILE_SIZE
        river.height = TILE_SIZE
        river.image = river.game.terrain2_spritesheet.get_sprite(3, 336, river.width, river.height)
        return river


class Furniture_door(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -1
        self.groups = self.game.all_sprites, self.game.furnitures_door
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # 讀取地板素材
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def door_path(cls, game, x, y):
        door_path = cls(game, x, y)
        door_path.width = TILE_SIZE
        door_path.height = TILE_SIZE
        door_path.image = door_path.game.terrain_spritesheet.get_sprite(3, 336, door_path.width, door_path.height)
        door_path.rect = door_path.image.get_rect()
        door_path.rect.x = door_path.x
        door_path.rect.y = door_path.y
        return door_path


class River_Block_door(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -3
        self.groups = self.game.all_sprites, self.game.river_blocks_door
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # 讀取地板素材
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @classmethod
    def grass(cls, game, x, y):
        grass = cls(game, x, y)
        grass.width = TILESIZE
        grass.height = TILESIZE
        grass.image = grass.game.terrain_spritesheet.get_sprite(128, 192, grass.width, grass.height)
        grass.rect = grass.image.get_rect()
        grass.rect.x = grass.x
        grass.rect.y = grass.y
        return grass
