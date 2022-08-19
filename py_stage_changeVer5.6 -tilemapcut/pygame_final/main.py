import pygame
import time
import sys
import os
from setting import *
from sprites import *
from font import *
from statement_view import Statement_View
#from font2  import *


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.font = pygame.font.Font("txt/Silver.ttf", 20)
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 設定視窗大小
        pygame.display.set_caption("keep in safe")
        self.clock = pygame.time.Clock()  # 設定時間
        self.running = True
        self.restart = True
        self.fade_in = True
        self.in_short_intro = True
        self.fade_out = False
        self.fade_in_counter = 255
        self.fade_in_from_black = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.fade_in_from_black.fill((0, 0, 0))



        self.character_spritesheet = SpriteSheet('img/man.png')
        self.terrain_spritesheet = SpriteSheet('img/terrain.png')


        self.character_spritesheet = SpriteSheet('img/man .png')
        self.terrain2_spritesheet = SpriteSheet('img/terrain4.png')
        self.buliding_spritesheet = SpriteSheet('img/street .png')
        self.furniture_spritesheet = SpriteSheet('img/f.png')
        self.store_spritesheet  = SpriteSheet("img/bag.png")

        self.entry = pygame.transform.scale(pygame.image.load("img/intro/game_Start.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.test = pygame.transform.scale(pygame.image.load("img/intro/tortus.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.black = pygame.transform.scale(pygame.image.load("img/black.png"), (WIN_WIDTH, WIN_HEIGHT))

        self.entry_music = r'music/begining.mp3'  # 音樂測試
        self.walk_effect = r'music/walking_on_a_floor.mp3'
        # 地圖參數
        self.map_change = False
        self.maps = [tilemap_0, tilemap_house, tilemap_river]
        self.map_number = 0
        self.shop_is_open = False
        self.shop_count = 0
        #錢錢
        self.money = 200
        # 物品籃
        # 0:noodle, #1 tape, #2water #3 Cola #4 Toy
        self.item_bag = [0, 0, 0, 0, 0, 0, 0, 0]
        #NPC觸發旗標
        self.touch_NPC = False
        self.npc_choose = 0
        self.talk_trigger = False
        self.counter = 0
        # interface
        self.view = Statement_View(self)

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        # self.terrains.update()
        self.doors.update()
        self.floors.update()
        self.furnitures.update()
        self.furnitures_door.update()
        self.all_sprites.update()
        self.blocks.update()
        self.player.update()

        self.river_grounds.update()
        self.river_blocks.update()
        self.river_blocks_door.update()

        self.store_detectors.update()
        self.store.update()

        self.NPCS_river.update()
        self.view.update()

    def events(self):
        self.clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if not self.shop_is_open:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        # self.running = False
                    # 切換場景範例
                    if event.key == pygame.K_n:
                        if self.map_number == 1:
                            self.change_stage(0)
                        elif self.map_number == 0:
                            self.change_stage(1)
                    if event.key == pygame.K_w:
                        if self.map_number == 2:
                            self.change_stage(0)
                        elif self.map_number == 0:
                            self.change_stage(2)
                    if event.key == pygame.K_q:
                        self.shop()
                elif self.shop_is_open:
                    if event.key == pygame.K_n:
                        self.all_sprites.switch_layer(6, -6)
                        self.shop_count = 0
                        self.shop_is_open = False
                    if event.key == pygame.K_1:
                        if self.money >= NOODLE_PRICE:
                            self.money -= NOODLE_PRICE
                            self.item_bag[0] += 1
                    elif event.key == pygame.K_2:
                        if self.money >= TAPE_PRICE:
                            self.money -= TAPE_PRICE
                            self.item_bag[1] += 1
                    elif event.key == pygame.K_3:
                        if self.money >= WATER_PRICE:
                            self.money -= WATER_PRICE
                            self.item_bag[2] += 1
                    elif event.key == pygame.K_4:
                        if self.money >= COLA_PRICE:
                            self.money -= COLA_PRICE
                            self.item_bag[3] += 1
                    elif event.key == pygame.K_5:
                        if self.money >= TOY_PRICE:
                            self.money -= TOY_PRICE
                            self.item_bag[4] += 1    
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.grounds = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

        self.player = pygame.sprite.LayeredUpdates()
        self.NPCS_floor = pygame.sprite.LayeredUpdates()
        self.NPCS_ground = pygame.sprite.LayeredUpdates()
        self.NPCS_river = pygame.sprite.LayeredUpdates()


        self.floors = pygame.sprite.LayeredUpdates()
        self.furnitures = pygame.sprite.LayeredUpdates()
        self.furnitures_door = pygame.sprite.LayeredUpdates()

        self.river_grounds = pygame.sprite.LayeredUpdates()
        self.river_blocks = pygame.sprite.LayeredUpdates()
        self.river_blocks_door =pygame.sprite.LayeredUpdates()

        self.store_detectors = pygame.sprite.LayeredUpdates()
        self.store =pygame.sprite.LayeredUpdates()

        self.createmap()
        self.walk_sound = pygame.mixer.Sound(self.walk_effect)
        self.walk_sound.set_volume(0.1)

    def gameover(self):
        pygame.quit()
        sys.exit()

    def entry_screen(self):
        self.restart = False
        in_entry_screen = True
        self.font = pygame.font.Font("txt/Silver.ttf", 40)
        intro_text = Font().get_text('txt/start.txt')
        intro_text_image = self.font.render(intro_text, True, (255, 255, 255))
        counter = 0
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        while in_entry_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    in_entry_screen = False
                    self.in_short_intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        self.in_short_intro = False
                        in_entry_screen = False
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        in_entry_screen = False

            intro_text_image.set_alpha(counter)
            self.screen.blit(self.entry, (0, 0))
            self.screen.blit(intro_text_image, (500, 700))
            self.clock.tick(FPS)
            pygame.display.update()
            if self.fade_in:
                counter += 2
            if self.fade_out:
                counter -= 2
            if counter >= 255:
                self.fade_out = True
                self.fade_in = False
            if counter == 0:
                self.fade_in = True
                self.fade_out = False

        # tilemap set

    def createmap(self):
        for map in self.maps:
            for i, row in enumerate(map):
                for j, column in enumerate(row):
                    # 底層全鋪
                    if self.map_number == 0:
                        Ground.terrainC(self, j, i)
                    elif self.map_number == 1:
                        Floor.road(self, j, i)
                    elif self.map_number == 2:
                        River_Ground.modA(self, j, i)
                        # 判斷物件
                    if column == "/":
                        Ground.terrainA(self, j, i)
                    elif column == "O":
                        Ground.modA(self, j, i)
                    elif column == "1":
                        Ground.rockB(self, j, i)
                    elif column == "g":
                        Ground.road(self, j, i)
                    elif column == 'H':
                        Block.house(self, j, i)
                    elif column == 'R':
                        Block.river(self, j, i)
                    elif column == 'S':
                        Block.shop(self, j, i)
                    elif column == 'P':
                        Player(self, j, i)
                    elif column == 'd':
                        Door.house(self, j, i)
                        Ground.modA(self, j, i)
                    elif column == 'r':
                        Door.river(self, j, i)
                        Ground.modA(self, j, i)
                    elif column == 'b':
                        Floor.road(self, j, i)
                        Furniture.bed(self, j, i)
                    elif column == '#':
                        Furniture_door.door_path(self, j, i)
                    elif column == "+":
                        River_Ground.terrainC(self, j, i)
                    elif column == "c":
                        River_Ground.waterA(self, j, i)
                    elif column == "-":
                        River_Ground.waterB(self, j, i)
                    elif column == "A":
                        River_Ground.modA(self, j, i)
                    elif column == "@":
                        River_Block_door.grass(self, j , i)
                    elif column =="q":
                        River_Ground.terrainC(self, j, i)
                        River_Block.stone(self, j, i)
                    elif column == '3':
                        if self.map_number == 2:
                            NPC_river(self, j, i)
                        elif self.map_number == 1:
                            NPC_Floor(self, j, i)
                    elif column == "_":
                        Store_detector.modA(self, j, i)
                    elif column =='$':
                        Store(self, j, i)
                    elif column == 'w':
                        Furniture.wall(self, j, i)
                    elif column =='V':
                        Floor.road(self, j, i)
                        Furniture.tv(self, j, i)
                    elif column == 's':
                        Floor.road(self, j, i)
                        Furniture.bookcase(self, j, i)
                    elif column == 'T':
                        Floor.road(self, j, i)
                        Furniture.table(self, j, i)
                    elif column == 'D':
                        Floor.road(self, j, i)
                        Furniture.chair(self, j, i)
                    elif column == '~':
                        Floor.road(self, j, i)
                        Furniture.table2(self, j, i)
                    elif column == 'l':
                        Floor.road(self, j, i)
                        Furniture.sofa(self, j, i)
                    elif column == 'C':
                        Floor.road(self, j, i)
                        Furniture.sofa2(self, j, i)
                    elif column == 'G':
                        NPC_river.gold(self, j, i)



            self.map_number += 1

    def short_intro(self):

        part_counter = 0
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font("txt/Silver.ttf", 30)
        self.screen.blit(self.black, (0, 0))

        counter = 0

        while self.in_short_intro:
            space_image = self.font.render(space, True, (255, 255, 255))
            space_image.set_alpha(counter)
            self.screen.blit(space_image, (600, 750))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    self.in_short_intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        self.in_short_intro = False

                    if event.key == pygame.K_SPACE:

                        if part_counter == 7:
                            self.screen.blit(self.black, (0, 0))
                            self.in_short_intro = False
                            pygame.mixer.music.stop()
                            self.map_number = 0
                        else:
                            if part_counter == 0:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                            if part_counter == 1:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                            if part_counter == 2:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                            if part_counter == 3:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                            if part_counter == 4:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))
                            if part_counter == 4:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))

                            if part_counter == 5:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))
                                self.screen.blit(self.font.render(dad3, True, (255, 255, 255)), (400, 600))
                            if part_counter == 6:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(week, True, (255, 255, 255)), (500, 400))

                            part_counter += 1

            self.clock.tick(FPS)

            pygame.display.update()
            if self.fade_in:
                counter += 2
            if self.fade_out:
                counter -= 2
            if counter >= 255:
                self.fade_out = True
                self.fade_in = False
            if counter == 0:
                self.fade_in = True
                self.fade_out = False

    def change_stage(self, dst_stage):
        if dst_stage == 1:
            self.map_number = dst_stage
            print(f'before: {self.all_sprites.layers()}')
            self.all_sprites.switch_layer(-1, 4)
            self.all_sprites.switch_layer(-2, 3)
            self.all_sprites.switch_layer(2, -1)
            self.all_sprites.switch_layer(1, -2)
            print(f'after: {self.all_sprites.layers()}')

        elif dst_stage == 0:
            if self.map_number == 1:
                print(f'before: {self.all_sprites.layers()}')
                self.all_sprites.switch_layer(-1, 2)
                self.all_sprites.switch_layer(-2, 1)
                self.all_sprites.switch_layer(4, -1)
                self.all_sprites.switch_layer(3, -2)
                print(f'after: {self.all_sprites.layers()}')
            if self.map_number == 2:
                print(f'before: {self.all_sprites.layers()}')
                print("Block layer:" + str(self.river_blocks.layers()) + "BLOCK door layer：" + str(
                    self.river_blocks_door.layers()))
                self.all_sprites.switch_layer(-3, 2)
                self.all_sprites.switch_layer(-4, 1)
                self.all_sprites.switch_layer(4, -3)
                self.all_sprites.switch_layer(3, -4)
                print(f'after: {self.all_sprites.layers()}')
                print("Block layer:"+str(self.river_blocks.layers())+"BLOCK door layer："+str(self.river_blocks_door.layers()))
            self.map_number = dst_stage

        elif dst_stage == 2:
            self.map_number = dst_stage
            print(f'before: {self.all_sprites.layers()}')
            self.all_sprites.switch_layer(-3, 4)
            self.all_sprites.switch_layer(-4, 3)
            self.all_sprites.switch_layer(2, -3)
            self.all_sprites.switch_layer(1, -4)
            print(f'after: {self.all_sprites.layers()}')

    def shop(self):
        if self.shop_count == 0:
            print(self.store.layers())
            self.all_sprites.switch_layer(-6, 6)

            Store(self, 1100, 750)
            self.shop_count += 1
            print(self.shop_count)

    def NPC_touch(self):

        if not self.shop_is_open:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.touch_NPC:
                            if self.map_number ==0:
                                pass
                            elif self.map_number == 1:
                                pass
                            elif self.map_number == 2:
                                if self.counter ==0: #and self.npc_choose == 0:
                                    self.screen.blit(self.font.render("飢餓程度", True, (255, 255, 255)), (1000, 650))

                                    self.counter+=1

                                elif self.counter == 1:
                                    self.screen.fill(BLACK)
                                    self.screen.blit(self.font.render("RRRRRR", True, (255, 255, 255)), (1000, 650))
                                    self.counter+=1
                                    self.money+=100
                                elif self.counter == 2:
                                    self.screen.fill(BLACK)
                                    self.counter+=1
                                    self.touch_NPC = False
                                elif self.counter >= 3 and self.counter%2 == 1:
                                    self.screen.blit(self.font.render("RR", True, (255, 255, 255)), (1000, 650))
                                    self.counter += 1
                                elif self.counter >= 3 and self.counter%2 == 0:
                                    self.screen.fill(BLACK)
                                    self.counter += 1
                                    self.touch_NPC = False
                            #elif self.counter == 0 :#and self.npc_choose ==1:
                            #    self.screen.blit(self.font.render("撿到黃金", True, (255, 255, 255)), (1000, 810))














    def main(self):
        # loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False


game = Game()
while game.restart:
    game = Game()
    game.new()
    game.entry_screen()
    game.short_intro()

    while game.running:
        game.main()
pygame.quit()
sys.exit()
