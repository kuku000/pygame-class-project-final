import pygame
from setting import *
import setting
from font import *
from player import Player
from base_elements import *
from block_elements import *
from doors import*



class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((255, 255, 255))
        # sprite.set_colorkey((0, 0, 0))
        return sprite

    def get_sprite2(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey((0, 0, 0))
        return sprite

# __________________NPC因為每一個地圖都在不同層 所以每層的NPC 都得自己創一個Class_____________________
class NPC_Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 設置 NPC 所處的層
        self.game = game
        self._layer = 1
        self.groups = self.game.all_sprites, self.game.NPCS_ground
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.name = 'posiyn'
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = 2 * TILE_SIZE
        self.height = 2 * TILE_SIZE
        # 初始化NPC圖案(色塊)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        # 設置 NPC 路徑
        self.path = KING_PATH
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
        self.image = self.game.store_spritesheet.get_sprite(0, 0, 225, 256)

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


class Sandbag(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = -7
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


class Sandbag_detector(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = -4
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
