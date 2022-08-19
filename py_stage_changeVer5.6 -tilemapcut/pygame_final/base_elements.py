import pygame
from setting import *


class Ground(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.grounds
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
    def terrainA(cls, game, x, y):
        terrainA = cls(game, x, y)
        terrainA.width = TILE_SIZE
        terrainA.height = TILE_SIZE
        terrainA.image = terrainA.game.terrain_spritesheet.get_sprite(192, 192, terrainA.width, terrainA.height)
        return terrainA

    @classmethod
    def terrainB(cls, game, x, y):
        terrainB = cls(game, x, y)
        terrainB.width = TILE_SIZE
        terrainB.height = TILE_SIZE
        terrainB.image = terrainB.game.terrain_spritesheet.get_sprite(256, 192, terrainB.width, terrainB.height)
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
        modA.image = modA.game.terrain_spritesheet.get_sprite(0, 231, modA.width, modA.height)
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

    @classmethod
    def waterA(cls, game, x, y):
        waterA = cls(game, x, y)
        waterA.width = TILE_SIZE
        waterA.height = TILE_SIZE
        waterA.image = waterA.game.terrain_spritesheet.get_sprite(1, 300, waterA.width, waterA.height)
        return waterA

    @classmethod
    def waterB(cls, game, x, y):
        waterB = cls(game, x, y)
        waterB.width = TILE_SIZE
        waterB.height = TILE_SIZE
        waterB.image = waterB.game.terrain_spritesheet.get_sprite(TILESIZE + 2, 300, waterB.width, waterB.height)
        return waterB

    def update(self):
        pass


class Floor(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -2
        self.groups = self.game.all_sprites, self.game.floors
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
    def road(cls, game, x, y):
        road = cls(game, x, y)
        road.width = TILE_SIZE
        road.height = TILE_SIZE
        road.image = road.game.terrain2_spritesheet.get_sprite(3, 336, road.width, road.height)
        return road

    def update(self):
        pass


class River_Ground(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -4
        self.groups = self.game.all_sprites, self.game.river_grounds
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
    def modA(cls, game, x, y):
        modA = cls(game, x, y)
        modA.width = TILE_SIZE
        modA.height = TILE_SIZE
        modA.image = modA.game.terrain_spritesheet.get_sprite(0, 231, modA.width, modA.height)
        return modA

    @classmethod
    def terrainC(cls, game, x, y):
        terrainC = cls(game, x, y)
        terrainC.width = TILE_SIZE
        terrainC.height = TILE_SIZE
        terrainC.image = terrainC.game.terrain_spritesheet.get_sprite(128, 192, terrainC.width, terrainC.height)
        return terrainC

    @classmethod
    def waterA(cls, game, x, y):
        waterA = cls(game, x, y)
        waterA.width = TILE_SIZE
        waterA.height = TILE_SIZE
        waterA.image = waterA.game.terrain_spritesheet.get_sprite(1, 300, waterA.width, waterA.height)
        return waterA

    @classmethod
    def waterB(cls, game, x, y):
        waterB = cls(game, x, y)
        waterB.width = TILE_SIZE
        waterB.height = TILE_SIZE
        waterB.image = waterB.game.terrain_spritesheet.get_sprite(TILESIZE + 2, 300, waterB.width, waterB.height)
        return waterB

    def update(self):
        pass