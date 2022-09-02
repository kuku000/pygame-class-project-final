import pygame
from setting import *
import setting
from font import *
from player import Player
from base_elements import *
from block_elements import *
from doors import *


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 255, 255))
        return sprite

    def get_sprite2(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def get_sprite_scale1(self, x, y, width, height):
        pygame.transform.scale(self.sheet, (width, height))
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 255, 255))
        return sprite


# __________________NPC因為每一個地圖都在不同層 所以每層的NPC 都得自己創一個Class_____________________
class NPC_Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        self._layer = 2
        self.groups = self.game.all_sprites, self.game.NPCS_ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.name = 'king'
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 64
        self.height = 64
        # 初始化NPC圖案(色塊)
        self.image = self.game.character_spritesheet.get_sprite(73, 517, self.width, self.height)
        # self.image = pygame.Surface([64,64])
        # self.image.fill(BLUE)
        # 設置 NPC 路徑
        # self.path = KING_PATH
        self.path_pos = 0
        # 設置 NPC 面向
        self.facing = 'down'
        self.animation_loop = 1
        # 設置 NPC 移動
        self.moving = False
        self.x_change = 0
        self.y_change = 0
        self.speed = 2
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

        self.path_pos += 1

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

    def move_detection(self):
        pass


class NPC_Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        self._layer = -1
        self.groups = self.game.all_sprites, self.game.NPCS_floor
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.name = 'Losin'
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2 * TILE_SIZE
        self.height = 2 * TILE_SIZE
        # 初始化NPC圖案(色塊)
        self.image = self.game.character_spritesheet.get_sprite(8.2 * TILESIZE, 13.6 * TILESIZE, self.width,
                                                                self.height)
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

        self.path_pos += 1

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

    def move_detection(self):
        pass

    @classmethod
    def tv(cls, game, x, y):
        tv = cls(game, x, y)
        tv.name = "tv"
        tv.width = 100
        tv.height = 79
        tv.image = tv.game.furniture_spritesheet.get_sprite2(377, 23, tv.width, tv.height)
        tv.rect = tv.image.get_rect()
        tv.rect.x = tv.x
        tv.rect.y = tv.y
        return tv

    @classmethod
    def box(cls, game, x, y):
        box = cls(game, x, y)
        box.name = "box"
        box.width = 32
        box.height = 38
        box.image = box.game.furniture_spritesheet.get_sprite2(134, 274, box.width, box.height)
        box.rect = box.image.get_rect()
        box.rect.x = box.x
        box.rect.y = box.y
        return box

    @classmethod
    def win1(cls, game, x, y):
        win = cls(game, x, y)
        win.name = "win1"
        win.width = 32
        win.height = 32
        win.image = win.game.terrain2_spritesheet.get_sprite(230, 302, win.width, win.height)
        win.rect = win.image.get_rect()
        win.rect.x = win.x
        win.rect.y = win.y
        return win

    @classmethod
    def win2(cls, game, x, y):
        win = cls(game, x, y)
        win.name = "win2"
        win.width = 32
        win.height = 32
        win.image = win.game.terrain2_spritesheet.get_sprite(230, 302, win.width, win.height)
        win.rect = win.image.get_rect()
        win.rect.x = win.x
        win.rect.y = win.y
        return win

    @classmethod
    def sandbag(cls, game, x, y):
        sanbag = cls(game, x, y)
        sanbag.name = "sandbag_d"
        sanbag._layer = 4
        sanbag.width = TILE_SIZE
        sanbag.height = TILE_SIZE
        sanbag.image = sanbag.game.terrain2_spritesheet.get_sprite(3, 336, sanbag.width, sanbag.height)
        sanbag.rect = sanbag.image.get_rect()
        sanbag.rect.x = sanbag.x
        sanbag.rect.y = sanbag.y
        return sanbag


class NPC_river(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        self._layer = -3
        self.groups = self.game.all_sprites, self.game.NPCS_river
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.name = 'river_man'
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2 * TILE_SIZE
        self.height = 2 * TILE_SIZE
        # 初始化NPC圖案(色塊)
        self.image = self.game.character_spritesheet.get_sprite(8.2 * TILESIZE, 11.6 * TILESIZE, self.width,
                                                                self.height)
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

        self.path_pos += 1

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

    def move_detection(self):
        pass

    def update(self) -> None:
        # self.npc_detect()
        # self.game.NPC_touch()
        pass

    @classmethod
    def gold(cls, game, x, y):
        gold = cls(game, x, y)
        gold.name = "gold"
        gold.width = TILESIZE
        gold.height = TILESIZE
        gold.image = gold.game.buliding_spritesheet.get_sprite(264, 285, gold.width, gold.height)
        gold.rect = gold.image.get_rect()
        gold.rect.x = gold.x
        gold.rect.y = gold.y
        return gold


class Store(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = -6
        self.groups = self.game.all_sprites, self.game.store
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        # 讀取地板素材
        self.image = self.game.store_spritesheet.get_sprite(0, 0, 320, 256)

        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self) -> None:
        pass


class Store_detector(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.store_detectors
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

    def update(self) -> None:
        pass

    @classmethod
    def modA(cls, game, x, y):
        modA = cls(game, x, y)
        modA.width = TILE_SIZE
        modA.height = TILE_SIZE
        modA.image = modA.game.terrain_spritesheet.get_sprite(0, 231, modA.width, modA.height)
        return modA


class Money_item(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = -1
        self.groups = self.game.all_sprites, self.game.money_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 42
        self.height = 22
        # 讀取地板素材
        self.image = self.game.buliding_spritesheet.get_sprite(258, 450, self.width, self.height)

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

    def update(self) -> None:
        pass


class Sandbag_detector(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = 6
        self.groups = self.game.all_sprites, self.game.sandbag_trigger
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

    def update(self):
        pass

    @classmethod
    def sandbag_detect(cls, game, x, y):
        sandbag_detect = cls(game, x, y)
        sandbag_detect.name = "sanbag_d"
        sandbag_detect.width = TILE_SIZE
        sandbag_detect.height = TILE_SIZE
        sandbag_detect.image = sandbag_detect.game.terrain2_spritesheet.get_sprite(3, 336, sandbag_detect.width,
                                                                                   sandbag_detect.height)
        sandbag_detect.rect = sandbag_detect.image.get_rect()
        sandbag_detect.rect.x = sandbag_detect.x
        sandbag_detect.rect.y = sandbag_detect.y
        return sandbag_detect

    @classmethod
    def sandbag(cls, game, x, y):
        sandbag = cls(game, x, y)
        sandbag.name = "sanbag"
        sandbag.width = TILE_SIZE
        sandbag.height = TILE_SIZE
        sandbag.image = sandbag.game.object_spritesheet.get_sprite(83, 56, sandbag.width, sandbag.height)
        sandbag.rect = sandbag.image.get_rect()
        sandbag.rect.x = sandbag.x
        sandbag.rect.y = sandbag.y
        return sandbag


class Clues(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = -8
        self.groups = self.game.all_sprites, self.game.cluepaper
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)

        # 讀取地板位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self) -> None:
        pass

    @classmethod
    def clue1(cls, game, x, y):
        clue1 = cls(game, x, y)
        clue1.width = 162
        clue1.height = 118
        clue1.image = clue1.game.clue1_spritesheet.get_sprite(0, 0, clue1.width, clue1.height)
        clue1.rect = clue1.image.get_rect()
        clue1.rect.x = clue1.x
        clue1.rect.y = clue1.y
        return clue1

    @classmethod
    def clue2(cls, game, x, y):
        clue2 = cls(game, x, y)
        clue2.width = 101
        clue2.height = 101
        clue2.image = clue2.game.clue2_spritesheet.get_sprite(0, 0, clue2.width, clue2.height)
        clue2.rect = clue2.image.get_rect()
        clue2.rect.x = clue2.x
        clue2.rect.y = clue2.y
        return clue2

class Windows_detector(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = 6
        self.groups = self.game.all_sprites, self.game.windows_trigger
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

    def update(self):
        pass

    @classmethod
    def window_pasted(cls, game, x, y):
        window_pasted = cls(game, x, y)
        window_pasted.name = "windowpasted"
        window_pasted.width = TILE_SIZE
        window_pasted.height = TILE_SIZE
        window_pasted.image = window_pasted.game.terrain2_spritesheet.get_sprite(3, 268, window_pasted.width, window_pasted.height)
        window_pasted.rect = window_pasted.image.get_rect()
        window_pasted.rect.x = window_pasted.x
        window_pasted.rect.y = window_pasted.y
        return window_pasted