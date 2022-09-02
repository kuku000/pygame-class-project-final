import pygame
from setting import *


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER

        self.groups = self.game.all_sprites, self.game.blocks
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
        house.width = 224
        house.height = 192
        house.image = house.game.buliding_spritesheet.get_sprite(19, 60, house.width, house.height)
        house.rect = house.image.get_rect()
        house.rect.x = house.x
        house.rect.y = house.y
        return house

    @classmethod
    def river(cls, game, x, y):
        river = cls(game, x, y)
        river.width = 160
        river.height = 192
        river.image = river.game.buliding_spritesheet.get_sprite(10, 256, river.width, river.height)
        river.rect = river.image.get_rect()
        river.rect.x = river.x
        river.rect.y = river.y
        return river

    @classmethod
    def shop(cls, game, x, y):
        shop = cls(game, x, y)
        shop.width = 160
        shop.height = 160
        shop.image = shop.game.buliding_spritesheet.get_sprite(252, 94, shop.width, shop.height)
        shop.rect = shop.image.get_rect()
        shop.rect.x = shop.x
        shop.rect.y = shop.y
        return shop

    @classmethod
    def bed(cls, game, x, y):
        bed = cls(game, x, y)
        bed.width = 160
        bed.height = 224
        bed.image = bed.game.furniture_spritesheet.get_sprite(250, 30, bed.width, bed.height)
        bed.rect = bed.image.get_rect()
        bed.rect.x = bed.x
        bed.rect.y = bed.y
        return bed

    @classmethod
    def flower(cls, game, x, y):
        flower = cls(game, x, y)
        flower.width = 40
        flower.height = 56
        flower.image = flower.game.buliding_spritesheet.get_sprite(408,309, flower.width, flower.height)
        flower.rect = flower.image.get_rect()
        flower.rect.x = flower.x
        flower.rect.y = flower.y
        return flower

    @classmethod
    def flower2(cls, game, x, y):
        flower2 = cls(game, x, y)
        flower2.width = 44
        flower2.height = 56
        flower2.image = flower2.game.buliding_spritesheet.get_sprite(462, 312, flower2.width, flower2.height)
        flower2.rect = flower2.image.get_rect()
        flower2.rect.x = flower2.x
        flower2.rect.y = flower2.y
        return flower2

    @classmethod
    def terrainA(cls, game, x, y):
        terrainA = cls(game, x, y)
        terrainA.width = TILE_SIZE
        terrainA.height = TILE_SIZE
        terrainA.image = terrainA.game.terrain_spritesheet.get_sprite(192, 192, terrainA.width, terrainA.height)
        return terrainA


class Furniture(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -1
        self.groups = self.game.all_sprites, self.game.furnitures
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
    def wall(cls, game, x, y):
        wall = cls(game, x, y)
        wall.width = TILESIZE
        wall.height = TILESIZE
        wall.image = wall.game.terrain2_spritesheet.get_sprite2(35, 336, wall.width, wall.height)
        wall.rect = wall.image.get_rect()
        wall.rect.x = wall.x
        wall.rect.y = wall.y
        return wall

    @classmethod
    def bed(cls, game, x, y):
        bed = cls(game, x, y)
        bed.width = 110
        bed.height = 150
        bed.image = bed.game.furniture_spritesheet.get_sprite2(40, 20, bed.width, bed.height)
        bed.rect = bed.image.get_rect()
        bed.rect.x = bed.x
        bed.rect.y = bed.y
        return bed

    @classmethod
    def tv(cls, game, x, y):
        tv = cls(game, x, y)
        tv.width = 100
        tv.height = 79
        tv.image = tv.game.furniture_spritesheet.get_sprite2(377, 23, tv.width, tv.height)
        tv.rect = tv.image.get_rect()
        tv.rect.x = tv.x
        tv.rect.y = tv.y
        return tv

    @classmethod
    def table(cls, game, x, y):
        table = cls(game, x, y)
        table.width = 57
        table.height = 58
        table.image = table.game.furniture_spritesheet.get_sprite2(36, 186, table.width, table.height)
        table.rect = table.image.get_rect()
        table.rect.x = table.x
        table.rect.y = table.y
        return table

    @classmethod
    def chair(cls, game, x, y):
        chair = cls(game, x, y)
        chair.width = 32
        chair.height = 58
        chair.image = chair.game.furniture_spritesheet.get_sprite2(207, 188, chair.width, chair.height)
        chair.rect = chair.image.get_rect()
        chair.rect.x = chair.x
        chair.rect.y = chair.y
        return chair

    @classmethod
    def bookcase(cls, game, x, y):
        bookcase = cls(game, x, y)
        bookcase.width = 83
        bookcase.height = 110
        bookcase.image = bookcase.game.furniture_spritesheet.get_sprite2(282, 24, bookcase.width, bookcase.height)
        bookcase.rect = bookcase.image.get_rect()
        bookcase.rect.x = bookcase.x
        bookcase.rect.y = bookcase.y
        return bookcase

    @classmethod
    def sofa(cls, game, x, y):
        sofa = cls(game, x, y)
        sofa.width = 43
        sofa.height = 58
        sofa.image = sofa.game.furniture_spritesheet.get_sprite2(251, 187, sofa.width, sofa.height)
        sofa.rect = sofa.image.get_rect()
        sofa.rect.x = sofa.x
        sofa.rect.y = sofa.y
        return sofa

    @classmethod
    def sofa2(cls, game, x, y):
        sofa2 = cls(game, x, y)
        sofa2.width = 43
        sofa2.height = 58
        sofa2.image = sofa2.game.furniture_spritesheet.get_sprite2(402, 187, sofa2.width, sofa2.height)
        sofa2.rect = sofa2.image.get_rect()
        sofa2.rect.x = sofa2.x
        sofa2.rect.y = sofa2.y
        return sofa2

    @classmethod
    def table2(cls, game, x, y):
        table2 = cls(game, x, y)
        table2.width = 88
        table2.height = 55
        table2.image = table2.game.furniture_spritesheet.get_sprite2(304, 186, table2.width, table2.height)
        table2.rect = table2.image.get_rect()
        table2.rect.x = table2.x
        table2.rect.y = table2.y
        return table2

    @classmethod
    def stone(cls, game, x, y):
        stone = cls(game, x, y)
        stone.width = TILESIZE
        stone.height = TILESIZE
        stone.image = stone.game.buliding_spritesheet.get_sprite(262, 333, stone.width, stone.height)
        stone.rect = stone.image.get_rect()
        stone.rect.x = stone.x
        stone.rect.y = stone.y
        return stone

    def update(self):
        pass


class River_Block(pygame.sprite.Sprite):  # 定義可路過的地板
    def __init__(self, game, x, y):
        # 遊戲開始設置地板的大小尺寸
        self.game = game
        self._layer = -3
        self.groups = self.game.all_sprites, self.game.river_blocks
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
    def stone(cls, game, x, y):
        stone = cls(game, x, y)
        stone.width = TILESIZE
        stone.height = TILESIZE
        stone.image = stone.game.buliding_spritesheet.get_sprite(262, 333, stone.width, stone.height)
        stone.rect = stone.image.get_rect()
        stone.rect.x = stone.x
        stone.rect.y = stone.y
        return stone

    @classmethod
    def tree(cls, game, x, y):
        tree = cls(game, x, y)
        tree.width = TILE_SIZE
        tree.height = TILE_SIZE
        tree.image = tree.game.buliding_spritesheet.get_sprite()

    def update(self):
        pass
