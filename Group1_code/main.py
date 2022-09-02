import pygame
import time
import sys
import os
from setting import *
from sprites import *
from font import *
from statement_view import Statement_View
from phasecontrollor import Phasecontrollor
from background_music_controllor import Background_music


class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.font = pygame.font.Font("txt/Silver.ttf", 35)
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

        self.terrain_spritesheet = SpriteSheet('img/terrain.png')
        self.character_spritesheet = SpriteSheet('img/character (2).png')
        self.terrain2_spritesheet = SpriteSheet('img/terrain4.png')
        self.buliding_spritesheet = SpriteSheet('img/street .png')
        self.furniture_spritesheet = SpriteSheet('img/furniture (1).png')

        self.store_spritesheet = SpriteSheet("img/shop.png")
        self.button_spritesheet = SpriteSheet("img/button1.png")
        self.dialog_spritesheet = SpriteSheet("img/dialogue_frame.png")

        self.clue1_spritesheet = SpriteSheet("img/paper1.png")
        self.clue2_spritesheet = SpriteSheet('img/paper2.png')

        self.object_spritesheet = SpriteSheet('img/object.png')

        self.entry = pygame.transform.scale(pygame.image.load("img/intro/game_Start.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.test = pygame.transform.scale(pygame.image.load("img/intro/tortus.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.black = pygame.transform.scale(pygame.image.load("img/black.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.die = pygame.transform.scale(pygame.image.load("img/die.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.win_pic = pygame.transform.scale(pygame.image.load("img/win.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.play_intro_pic = pygame.transform.scale(pygame.image.load("img/game instruction.png"), (WIN_WIDTH, WIN_HEIGHT))
        # 聲音
        self.entry_music = r'music/begining.mp3'
        self.walk_effect = r'music/walking_on_a_floor (mp3cut.net) (1).mp3'
        self.eat_noodle = r'music/eat.mp3'
        self.drink = pygame.mixer.Sound("music/drink.wav")
        # 河流背景
        self.river = r'music/river.mp3'
        self.river2 = pygame.mixer.Sound('music/mountain-river.wav')
        self.house_music = r'music/house.mp3'
        self.lose_music = r'music/Bad Clown.mp3'
        self.win_music = r'music/win.mp3'
        self.final_countdown = r'music/come.mp3'
        # 地圖參數
        self.map_change = False
        self.maps = [tilemap_0, tilemap_house, tilemap_river]
        self.map_number = 0
        self.shop_is_open = False
        self.shop_count = 0
        # 錢錢
        self.money = 200
        # 物品籃
        # 0:noodle,#1water #2 Cola #3 Toy #4 tape,
        self.item_bag = [0, 0, 0, 0, 0, 0, 0, 0]
        self.shortcut = [self.item_bag[0], self.item_bag[2], self.item_bag[3]]
        # NPC觸發旗標
        self.touch_NPC = False
        self.npc_choose = 0
        self.talk_trigger = False
        self.counter = 0  # 此地圖給第一個NPC
        self.counter2 = 0
        self.npc_name = None  # 回傳NPC名子
        self.in_talking = False  # 在對話時 鎖住頻目
        self.is_conversation = False
        # 對話選擇
        self.in_dialog = False  # 在選擇對話框
        self.choose = 0  # 選擇
        # 飢餓程度
        self.blood = 180

        # 勝利
        self.win = False
        # interface
        self.view = Statement_View(self)
        self.phase_center = Phasecontrollor(self)
        self.background_music = Background_music(self)

        self.clue_check = 0
        self.clue_counter = False
        self.sandbag_check = False

        self.change_sound = False

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):

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
        self.NPCS_ground.update()
        self.NPCS_floor.update()
        self.money_sprite.update()

        self.sandbag_trigger.update()
        self.windows_trigger.update()
        self.view.update()

    def events(self):
        self.font = pygame.font.Font("txt/Silver.ttf", 35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if self.shop_is_open:
                    if event.key == pygame.K_SPACE:
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
                            self.item_bag[4] += 1
                    elif event.key == pygame.K_3:
                        if self.money >= WATER_PRICE:
                            self.money -= WATER_PRICE
                            self.item_bag[1] += 1
                    elif event.key == pygame.K_4:
                        if self.money >= COLA_PRICE:
                            self.money -= COLA_PRICE
                            self.item_bag[2] += 1
                    elif event.key == pygame.K_5:
                        if self.money >= TOY_PRICE:
                            self.money -= TOY_PRICE
                            self.item_bag[3] += 1
                if self.is_conversation:
                    if event.key == pygame.K_SPACE:
                        self.phase_center.next_sentence()
                    elif event.key == pygame.K_1:
                        self.phase_center.selection(1)
                    elif event.key == pygame.K_2:
                        self.phase_center.selection(2)
                    elif event.key == pygame.K_3:
                        self.phase_center.selection(3)
                    elif event.key == pygame.K_4:
                        self.phase_center.selection(4)
                    elif event.key == pygame.K_5:
                        self.phase_center.selection(5)
                    elif event.key == pygame.K_6:
                        self.phase_center.selection(6)
                    elif event.key == pygame.K_7:
                        self.phase_center.selection(7)
                    elif event.key == pygame.K_8:
                        self.phase_center.selection(8)
                    elif event.key == pygame.K_9:
                        self.phase_center.selection(9)
                    elif event.key == pygame.K_0:
                        self.phase_center.selection(0)

                else:
                    if event.key == pygame.K_F1:
                        if self.item_bag[0] > 0 and self.blood != 180:
                            if self.blood + blood_plus[0] <= 180:
                                self.blood += blood_plus[0]
                            else:
                                self.blood = 180
                            self.eatting_noodle.play()
                            self.item_bag[0] -= 1

                    if event.key == pygame.K_F2:
                        if self.item_bag[1] > 0 and self.blood != 180:
                            if self.blood + blood_plus[1] <= 180:
                                self.blood += blood_plus[1]
                            else:
                                self.blood = 180
                            self.drink.play()
                            self.item_bag[1] -= 1
                    if event.key == pygame.K_F3:
                        if self.item_bag[2] > 0 and self.blood != 180:
                            if self.blood + blood_plus[2] <= 180:
                                self.blood += blood_plus[2]
                            else:
                                self.blood = 180
                            self.drink.play()
                            self.item_bag[2] -= 1
                    if event.key == pygame.K_F4:
                        if self.item_bag[3] > 0:
                            self.screen.fill(BLACK)
                            self.screen.blit(self.font.render("這東西似乎沒用處", True, (255, 255, 255)), (540, 650))
                            self.item_bag[3] -= 1
                        print(self.item_bag)
                    if event.key == pygame.K_h:
                        if self.clue_counter:
                            self.all_sprites.switch_layer(8, -8)
                            self.clue_counter = False
                        else:
                            self.all_sprites.switch_layer(-8, 8)
                            self.clue_counter = True
                        pygame.display.update()

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
        self.money_sprite = pygame.sprite.LayeredUpdates()

        self.floors = pygame.sprite.LayeredUpdates()
        self.furnitures = pygame.sprite.LayeredUpdates()
        self.furnitures_door = pygame.sprite.LayeredUpdates()

        self.river_grounds = pygame.sprite.LayeredUpdates()
        self.river_blocks = pygame.sprite.LayeredUpdates()
        self.river_blocks_door = pygame.sprite.LayeredUpdates()

        self.store_detectors = pygame.sprite.LayeredUpdates()
        self.store = pygame.sprite.LayeredUpdates()

        self.sandbag = pygame.sprite.LayeredUpdates()
        self.sandbag_trigger = pygame.sprite.LayeredUpdates()
        self.windows_trigger = pygame.sprite.LayeredUpdates()
        self.cluepaper = pygame.sprite.LayeredUpdates()

        self.createmap()
        self.walk_sound = pygame.mixer.Sound(self.walk_effect)
        self.walk_sound.set_volume(0.1)
        self.eatting_noodle = pygame.mixer.Sound(self.eat_noodle)
        self.walk_sound.set_volume(0.2)

    def gameover(self):
        pygame.mixer.quit()
        pygame.mixer.init()
        self.font = pygame.font.Font("txt/Silver.ttf",50)
        text_lose = self.font.render("Press space to restart", True, WHITE)
        text_win = self.font.render("Press space to restart", True, WHITE)
        counter = 0

        if self.win == False:
            pygame.mixer.music.load(self.lose_music)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(self.win_music)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)


        for sprite in self.all_sprites:
            sprite.kill()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    self.restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = False
                        self.playing = False
                        self.restart = True
            if self.win:
                self.screen.fill(BLACK)
                self.screen.blit(self.win_pic, (0,0))
                text_win.set_alpha(counter)
                self.screen.blit(text_win, (400, 700))
            elif self.win == False:

                self.screen.fill(BLACK)
                self.screen.blit(self.die, (0, 0))
                text_lose.set_alpha(counter)
                self.screen.blit(text_lose,(800, 700))
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
                        River_Block_door.grass(self, j, i)
                    elif column == "q":
                        River_Ground.terrainC(self, j, i)
                        River_Block.stone(self, j, i)
                    elif column == '3':
                        if self.map_number == 2:
                            NPC_river(self, j, i)
                        elif self.map_number == 1:
                            NPC_Floor(self, j, i)
                    elif column == "_":
                        Store_detector.modA(self, j, i)
                    elif column == '$':
                        Store(self, j, i)
                    elif column == 'w':
                        Furniture.wall(self, j, i)
                    elif column == 'V':
                        Floor.road(self, j, i)
                        NPC_Floor.tv(self, j, i)
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
                    elif column == 'F':
                        Block.flower(self, j, i)
                    elif column == "{":
                        Block.terrainA(self, j, i)
                    elif column == 'm':
                        Money_item(self, j, i)
                    elif column == 'j':
                        NPC_Ground(self, j, i)
                    elif column == ']':
                        NPC_Floor.box(self, j, i)
                    elif column == "W":
                        NPC_Floor.win1(self, j, i)
                    elif column == 'Z':
                        Clues.clue1(self, j, i)
                    elif column == 'X':
                        Clues.clue2(self, j, i)
                    elif column == '&':
                        NPC_Floor.win2(self, j, i)

            self.map_number += 1

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
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        self.in_short_intro = False
                        in_entry_screen = False
                        pygame.quit()
                        sys.exit()
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
    def play_intro(self):
        self.screen.fill(BLACK)
        self.restart = False
        in_play_intro_screen = True
        self.font = pygame.font.Font("txt/Silver.ttf", 40)
        intro_text_image = self.font.render("按space", True, (0, 0, 0))
        counter = 0

        while in_play_intro_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    self.in_short_intro = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        self.in_short_intro = False
                        in_play_intro_screen = False
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        in_play_intro_screen = False

            intro_text_image.set_alpha(counter)
            self.screen.blit(self.play_intro_pic, (0, 0))
            self.screen.blit(intro_text_image, (600, 700))
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



    def short_intro(self):

        part_counter = 0
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font("txt/Silver.ttf", 35 )
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
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        self.in_short_intro = False
                        pygame.quit()
                        sys.exit()
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
            self.background_music.music_choose()
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
                self.river2.fadeout(1)
                print(f'before: {self.all_sprites.layers()}')
                print("Block layer:" + str(self.river_blocks.layers()) + "BLOCK door layer：" + str(
                    self.river_blocks_door.layers()))
                self.all_sprites.switch_layer(-3, 2)
                self.all_sprites.switch_layer(-4, 1)
                self.all_sprites.switch_layer(4, -3)
                self.all_sprites.switch_layer(3, -4)
                print(f'after: {self.all_sprites.layers()}')
                print("Block layer:" + str(self.river_blocks.layers()) + "BLOCK door layer：" + str(
                    self.river_blocks_door.layers()))
            self.map_number = dst_stage
            self.background_music.music_choose()

        elif dst_stage == 2:
            self.map_number = dst_stage
            self.river2.fadeout(1)
            self.background_music.music_choose()
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
        if not self.shop_is_open and not self.is_conversation:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.touch_NPC:
                            print(self.npc_name)
                            self.is_conversation = True
                            if self.map_number == 0 and self.npc_name == 'king':
                                self.phase_center.talk_NPC0()
                            elif self.map_number == 1 and self.npc_name == 'Losin':
                                self.phase_center.talk_NPC1()
                            elif self.map_number == 2 and self.npc_name == 'river_man':
                                self.phase_center.talk_NPC2()
                            elif self.map_number == 2 and self.npc_name == 'gold':
                                self.phase_center.take_gold()
                            elif self.map_number == 1 and self.npc_name == 'tv':
                                self.phase_center.watch_TV()
                            elif self.map_number == 1 and self.npc_name == "win1":
                                self.phase_center.talk_window(1)
                            elif self.map_number == 1 and self.npc_name == "win2":
                                self.phase_center.talk_window(2)
                            elif self.map_number == 1 and self.npc_name == 'box':
                                self.phase_center.use_box()
                            elif self.map_number == 1 and self.npc_name == 'sanbag_d':
                                self.phase_center.put_sandbag()
    def start_hint(self):
        self.is_conversation = True
        self.phase_center.hint_message()

    def start_count(self):
        self.view.time_start()

    def check_win(self):
        return self.phase_center.check_win()

    def create_sandbag_detect(self):
        for i in range(17, 22):
            Sandbag_detector.sandbag_detect(self, i, 18)
        print(self.all_sprites.layers())

    def create_sandbags(self):
        for i in range(17, 22):
            Sandbag_detector.sandbag(self, i, 19)

    def create_windows_pasted2(self):
        for i in range(9,12):
            Windows_detector.window_pasted(self, 39, i)

    def create_windows_pasted1(self):
        for i in range(9,12):
            Windows_detector.window_pasted(self, 0, i)



    def main(self):
        # loop
        while self.playing:
            self.events()
            self.clock.tick(FPS)
            pygame.display.update()
            self.update()
            self.draw()


game = Game()
while game.restart:
    game = Game()
    game.new()
    game.entry_screen()
    game.play_intro()
    game.short_intro()
    game.background_music.music_choose()
    while game.running:
        game.main()
        game.gameover()
pygame.quit()
sys.exit()
