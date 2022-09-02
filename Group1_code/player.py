import random

import pygame
import math
from setting import *
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # 遊戲開始後，定義角色所處的層
        self.game = game
        self.need_change = False
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.player

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
        self.image = self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height)
        # 獲取角色位置
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.collidex = 0
        self.collidey = 0

        # 飢餓程度
        self.last_time = time.time()
        self.period = [20, 5, 1]

        self.dis_set = [192, 180]
        self.set = self.dis_set[0]

        self.blood = 180
        pygame.draw.rect(self.game.screen, WHITE, [blood_x, blood_y, 180, 40])
        pygame.draw.rect(self.game.screen, RED, [blood_x, blood_y, self.blood, 40])
        self.door_lock = False

        self.font = pygame.font.Font("txt/Silver.ttf", 35)

    def delete(self):
        pygame.sprite.Group.empty(self)

    def update(self):
        self.movement()
        self.animate()
        self.collide_money()

        self.rect.x += self.x_change
        if self.game.map_number == 0:
            self.collide_blocks('x')
            self.collide_door('x')
            self.collide_npcs('x')
        elif self.game.map_number == 1:
            self.collide_furnitures('x')
            self.collide_npcs('x')
        elif self.game.map_number == 2:
            self.collide_river_blocks('x')
            self.collide_river_blocks_door()
            self.collide_npcs('x')
        self.rect.y += self.y_change
        if self.game.map_number == 0:
            self.collide_blocks('y')
            self.collide_store_detector()
            self.collide_door('y')
            self.collide_npcs('y')
        elif self.game.map_number == 1:
            self.collide_furnitures('y')
            self.collide_furnitures_door()
            self.collide_npcs('y')
            if self.game.clue_check >=2:
                self.collide_trigger()
        elif self.game.map_number == 2:
            self.collide_river_blocks('y')
            self.collide_npcs('y')

        self.x_change = 0
        self.y_change = 0
        if self.need_change:
            self.need_change = False
            self.game.change_stage(self.next_stage)

        if self.game.shop_is_open:
            self.game.shop()
        elif self.game.shop_is_open == False:
            self.dis = self.dis_set[0]
        if self.door_lock:
            self.door_lock = False
            self.game.is_conversation = True
            self.game.start_hint()
            if self.game.map_number == 1:
                self.game.npc_name = 'door'
                self.game.touch_NPC = True
        self.game.NPC_touch()

    def movement(self):
        # 操控上下左右
        if not self.game.shop_is_open and not self.game.is_conversation:
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

    def collide_store_detector(self):
        hits = pygame.sprite.spritecollide(self, self.game.store_detectors, False)
        if hits:
            if self.y_change < 0:
                self.rect.y = hits[0].rect.bottom
                if hits[0].rect.top - self.height >= self.dis:
                    self.game.shop_is_open = True
                    self.dis = self.dis_set[1]

    def collide_blocks(self, direction):  # 角色碰撞方式
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction == "x":
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        # 如果綜向移動時撞到物品，角色停下
        elif direction == "y":
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    # 560新增
    def collide_furnitures_door(self):  # 角色碰撞方式
        hits = pygame.sprite.spritecollide(self, self.game.furnitures_door, False)
        if hits:
            if self.y_change > 0:
                self.rect.y = hits[0].rect.top - self.rect.height
                # print(hits[0].rect.bottom)
                if hits[0].rect.bottom >= 630:
                    if self.game.phase_center.goto_village():
                        self.need_change = True
                        self.next_stage = 0
                        self.rect.x = 896
                        self.rect.y = 280

    def collide_furnitures(self, direction):  # 角色碰撞方式
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.furnitures, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        # 如果綜向移動時撞到物品，角色停下

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.furnitures, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_river_blocks_door(self):  # 角色碰撞方式
        hits = pygame.sprite.spritecollide(self, self.game.river_blocks_door, False)
        if hits:
            if self.x_change < 0:
                self.rect.x = hits[0].rect.right
                if hits[0].rect.left - self.rect.width <= 32:
                    self.need_change = True
                    self.next_stage = 0
                    self.rect.x = 950
                    self.rect.y = 400

    def collide_door(self, direction):  # 角色碰撞方式
        hits = pygame.sprite.spritecollide(self, self.game.doors, False)
        # print(self.rect.y)
        if hits:
            if direction == 'x':
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left
                if hits[0].rect.x + self.rect.width >= 600:
                    if self.game.phase_center.goto_river():
                        self.need_change = True
                        self.next_stage = 2
                        self.rect.x = 64
                        self.rect.y = 300
                    else:
                        self.rect.x = 950
                        self.rect.y = 400
                        self.door_lock = True

            elif direction == 'y':
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.right
                if hits[0].rect.y - self.rect.height <= 400:
                    if self.game.phase_center.goto_house():
                        self.need_change = True
                        self.next_stage = 1
                        self.rect.x = 600
                        self.rect.y = 450

                    else:
                        self.rect.x = 896
                        self.rect.y = 280
                        self.door_lock = True

    def collide_river_blocks(self, direction):  # 角色碰撞方式
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.river_blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        # 如果綜向移動時撞到物品，角色停下

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.river_blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_npcs(self, direction):
        if self.game.map_number == 0:
            collidewith = self.game.NPCS_ground
            layer_choose_list = self.game.NPCS_ground.layers()
        elif self.game.map_number == 1:
            collidewith = self.game.NPCS_floor
            layer_choose_list = self.game.NPCS_floor.layers()
        elif self.game.map_number == 2:
            collidewith = self.game.NPCS_river
            layer_choose_list = self.game.NPCS_river.layers()
        if layer_choose_list == []:
            layer_choose = -100
        else:
            layer_choose = layer_choose_list[0]

        hits = pygame.sprite.spritecollide(self, collidewith, False)
        if (self.rect.x - self.collidex) ** 2 + (self.rect.y - self.collidey) > 64 ** 2:
            self.game.npc_name = None
            self.game.is_conversation = False
            self.game.touch_NPC = False
        if hits:
            for hit in hits:
                for i in range(len(collidewith.get_sprites_from_layer(layer_choose))):
                    if hit.name == collidewith.get_sprites_from_layer(layer_choose)[i].name:
                        self.game.npc_name = hit.name
                        self.collidex = hit.rect.x
                        self.collidey = hit.rect.y
            if direction == "x":
                self.game.touch_NPC = True
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

            # 如果綜向移動時撞到物品，角色停下
            if direction == "y":
                self.game.touch_NPC = True
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height

                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def collide_money(self):

        if self.game.map_number == 1:

            hits = pygame.sprite.spritecollide(self, self.game.money_sprite, True)
            if hits:
                money_get = random.choice([50, 100, 150, 200])
                self.game.money += money_get
                self.game.screen.fill(BLACK)
                self.game.screen.blit(self.font.render(f"超爽的~撿到{money_get}雷~", True, (255, 255, 255)),
                                      (540, 650))

    def collide_trigger(self):

        layer_choose_list = self.game.sandbag_trigger.layers()
        layer_choose = layer_choose_list[0]
        hits = pygame.sprite.spritecollide(self, self.game.sandbag_trigger, False)
        if (self.rect.x - self.collidex) ** 2 + (self.rect.y - self.collidey) > 64 ** 2:
            self.game.npc_name = None
            self.game.is_conversation = False
            self.game.touch_NPC = False
        if hits:
            for hit in hits:
                for i in range(len(self.game.sandbag_trigger.get_sprites_from_layer(layer_choose))):
                    if hit.name == self.game.sandbag_trigger.get_sprites_from_layer(layer_choose)[i].name:
                        self.game.npc_name = hit.name
                        self.collidex = hit.rect.x
                        self.collidey = hit.rect.y

            self.game.touch_NPC = True
            if self.y_change > 0:
                self.rect.y = hits[0].rect.top - self.rect.height
            if self.y_change < 0:
                self.rect.y = hits[0].rect.bottom


    def animate(self):  # 定義角色移動時動畫
        # 定義角色 向下 移動時圖片動畫
        down_animation = [
            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 2 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 2 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 2 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(8 * TILESIZE, 2 * TILESIZE, self.width, self.height)]
        # 定義角色 向上 移動時圖片動畫
        up_animation = [
            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 4.4 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 4.4 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 4.4 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(8 * TILESIZE, 4.4 * TILESIZE, self.width, self.height)]
        # 定義角色 向左 移動時圖片動畫
        left_animation = [
            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 6.8 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 6.8 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 6.8 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(8 * TILESIZE, 6.8 * TILESIZE, self.width, self.height)]
        # 定義角色 向右 移動時圖片動畫
        right_animation = [
            self.game.character_spritesheet.get_sprite(2 * TILESIZE, 9.3 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(4 * TILESIZE, 9.3 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(6 * TILESIZE, 9.3 * TILESIZE, self.width, self.height),
            self.game.character_spritesheet.get_sprite(8 * TILESIZE, 9.3 * TILESIZE, self.width, self.height)]
        # 如果角色是向下移動，則使角色圖片變為面向下的圖片包
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(2 * TILESIZE, 2 * TILESIZE, self.width,
                                                                        self.height)
            else:
                self.image = down_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向上移動，則使角色圖片變為面向上的圖片包
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(2 * TILESIZE, 4.4 * TILESIZE, self.width,
                                                                        self.height)
            else:
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向左移動，則使角色圖片變為面向左邊的圖片包
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(2 * TILESIZE, 6.8 * TILESIZE, self.width,
                                                                        self.height)
            else:
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
        # 如果角色是向右移動，則使角色圖片變為面向右邊的圖片包
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(2 * TILESIZE, 9.3 * TILESIZE, self.width,
                                                                        self.height)
            else:
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.game.walk_sound.play()
                    self.animation_loop = 1
