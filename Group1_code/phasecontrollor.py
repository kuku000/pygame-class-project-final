import time

import pygame

from sentence_words import *
from setting import *
from background_music_controllor import Background_music

class Phasecontrollor:
    # 初始化
    def __init__(self, game):
        self.game = game
        self.phase = 0
        self.phase_0_checklist = False
        # 0:NPC0(King) 1:NPC1(room_man) 2:NPC2(river_man) 3:gold_0 4:gold_1 5:TV 6:windows_1 7:Windows_2 8:BOX 9:door
        self.phase_1_checklist = [False, False, False, False, False, False, False, False, False]
        self.phase_2_checklist = [False, False, False, False, False, False, False, False, False]
        self.phase_3_checklist = [False, False, False, False, False, False, False, False, False, False]
        self.now_npc = None

        self.counter = 0
        self.selection_counter = -1
        self.now_dialog = None
        self.now_selection = None
        self.wait_for_select = False
        self.selector = -1
        self.end = False
        self.password = ''
        self.wait_password = False
        self.win_type = 0

        self.font = pygame.font.Font("txt/Silver.ttf", 35)

        self.background_music = Background_music(self)

        # Phase推進
    def phase_forward(self):
        self.phase += 1
        if self.phase == 3:
            pygame.mixer.music.load(self.game.final_countdown)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
            #self.background_music.change_Sound()

    # 各場景切換事件會根據PHASE判斷
    def goto_river(self):
        if self.phase == 0:
            if self.phase_0_checklist:
                return True
            else:
                return False
        elif self.phase == 1:
            return True
        elif self.phase == 2:
            return True

    def goto_house(self):
        if self.phase == 0:
            if self.phase_0_checklist:
                return True
            else:
                return False
        elif self.phase == 1:
            return True
        elif self.phase == 2:
            return True

    def goto_village(self):
        if self.game.map_number == 1:
            if self.phase == 3:
                return False
            else:
                return True

    # npc 對話，內容根據PHASE調整
    def talk_NPC0(self):
        self.now_npc = "king"
        if self.phase == 0:
            self.now_dialog = king_phase0
            self.phase_forward()
        elif self.phase == 1:
            self.now_dialog = king_junk_phase0
        elif self.phase == 2:
            if not self.phase_2_checklist[0]:
                self.phase_2_checklist[0] = True
                self.now_dialog = king_phase2
                self.game.money += 100
            elif self.phase_2_checklist[0]:
                self.now_dialog = king_junk_phase2
        self.print_dialog(self.now_dialog[self.counter])

    def talk_NPC1(self):
        self.now_npc = "room_man"
        if self.phase == 1:
            self.phase_1_checklist[1] = True
            self.now_dialog = room_man_phase1
        elif self.phase == 2:
            if not self.phase_2_checklist[2]:
                self.now_dialog = room_man_junk_phase2
            else:
                self.now_dialog = room_man_phase2
                self.selection_counter = 4
        elif self.phase == 3:
            if self.phase_3_checklist[1]:
                self.now_dialog = room_man_junk_phase3
            else:
                self.phase_3_checklist[1] = True
                self.selection_counter = 5
                self.now_dialog = room_man_phase3
        self.counter = 0
        self.print_dialog(self.now_dialog[self.counter])

    def talk_NPC2(self):
        self.now_npc = "riverman"
        if self.phase == 1:
            if not self.phase_1_checklist[2]:
                self.phase_1_checklist[2] = True
                self.selection_counter = 0
                self.now_dialog = river_man_phase1
            else:
                self.now_dialog = river_man_junk_phase1
        elif self.phase == 2:
            if not self.phase_2_checklist[2]:
                self.phase_2_checklist[2] = True
                self.game.clue_check += 1
                self.now_dialog = river_man_phase2
            else:
                self.now_dialog = river_man_junk_phase2

        self.counter = 0
        self.print_dialog(self.now_dialog[self.counter])

    # 黃金對話
    def take_gold(self):
        self.now_npc = "gold"
        if self.phase == 1:
            if not self.phase_1_checklist[3] and not self.phase_1_checklist[4]:
                self.phase_1_checklist[3] = True
                self.phase_1_checklist[4] = True
                self.now_dialog = gold_phase1
                self.game.money += 100
            else:
                self.now_dialog = gold_junk_phase1
        else:
            self.counter = 0
            self.selection_counter = 3
            self.game.money += 100
            self.now_dialog = gold_phase2
        self.print_dialog(self.now_dialog[self.counter])

    # 電視對話
    def watch_TV(self):
        self.now_npc = 'TV'
        if self.phase == 1:
            self.selection_counter = 2
            self.now_dialog = TV_phase1
        else:
            self.now_dialog = TV_answer1_phase1
        self.print_dialog(self.now_dialog[self.counter])

    # 窗戶對話
    def talk_window(self, type):
        self.now_npc = "windows"
        if self.phase == 3:
            if type == 1:
                if self.phase_3_checklist[6]:
                    self.counter = 0
                    self.now_dialog = windows_junk_phase3
                elif self.game.item_bag[4] <=0:
                    self.counter = 0
                    self.now_dialog = windows_junk_lose
                else:
                    self.selection_counter = 6
                    self.counter = 0
                    self.now_dialog = windows_phase3
                    self.win_type = 1

            elif type == 2:
                if self.phase_3_checklist[7]:
                    self.counter = 0
                    self.now_dialog = windows_junk_phase3
                elif self.game.item_bag[4] <= 0:
                    self.counter = 0
                    self.now_dialog = windows_junk_lose
                else:
                    self.selection_counter = 6
                    self.counter = 0
                    self.now_dialog = windows_phase3
                    self.win_type = 2

        else:
            self.counter = 0
            self.now_dialog = windows_phase1
            print('talk window')
        self.print_dialog(self.now_dialog[self.counter])

    # 道具箱對話
    def use_box(self):
        self.now_npc = 'box'
        if self.phase == 3:
            if self.phase_3_checklist[8]:
                self.now_dialog = box_phase1
            else:
                self.now_dialog = box_phase3
                self.password = ''
                self.wait_password = True
        else:
            self.now_dialog = box_phase1
        self.counter = 0
        self.print_dialog(self.now_dialog[self.counter])

    def put_sandbag(self):
        self.now_npc = 'door'
        if self.phase == 3:
            if self.phase_3_checklist[9]:
                self.now_dialog = door_answer1_phase3
                print('now_dialog = door')
            else:
                self.now_dialog = door_phase3
                self.selection_counter = 7
                print("door_phase")
        self.counter = 0
        self.print_dialog(self.now_dialog[self.counter])

    # 提示訊息
    def hint_message(self):
        self.now_npc = "hint"
        self.now_dialog = phase0_hint
        self.print_dialog(self.now_dialog[self.counter])


    # 印出字體作用
    def print_dialog(self, string):
        if string != 'selections':
            pygame.draw.rect(self.game.screen, BLACK, pygame.Rect(516, 640, 764, 160))
            self.game.screen.blit(self.font.render(
                string, True, WHITE), (520, 650))
            self.game.screen.blit(self.font.render(
                '繼續(space)', True, WHITE), (1140, 750))
        else:
            self.now_selection = selectionsGroup[self.selection_counter]
            self.wait_for_select = True
            self.print_selections(self.now_selection[0], self.now_selection[1])

    # 印出選項

    def print_selections(self, stringA, stringB):
        pygame.draw.rect(self.game.screen, BLACK, pygame.Rect(516, 640, 764, 160))
        self.game.screen.blit(self.font.render(
            stringA, True, WHITE), (520, 650))
        self.game.screen.blit(self.font.render(
            stringB, True, WHITE), (520, 682))

    # 清空對話框

    def print_Blank(self):
        pygame.draw.rect(self.game.screen, BLACK, pygame.Rect(516, 640, 764, 160))
        self.counter = 0

    # 密碼檢查
    def check_password(self):
        print(self.password)
        if self.password == '5478':
            self.now_dialog = box_answer0_phase3
            self.phase_3_checklist[8] = True
        else:
            self.now_dialog = box_answer1_phase3
        self.counter = 0
        self.password = ''
        self.wait_password = False
        self.print_dialog(self.now_dialog[self.counter])

    # 下一句 給空白鍵事件用

    def next_sentence(self):
        if not self.wait_for_select:
            self.counter += 1
            if self.counter < (len(self.now_dialog)):
                if self.now_dialog[self.counter] != 'selections':
                    self.print_dialog(self.now_dialog[self.counter])
                elif self.now_dialog[self.counter] == 'selections':
                    self.now_selection = selectionsGroup[self.selection_counter]
                    self.print_selections(self.now_selection[0], self.now_selection[1])
                    self.wait_for_select = True
            else:
                self.now_npc = ""
                if self.wait_password:
                    self.check_password()
                else:
                    self.now_dialog = None
                    self.counter = 0
                    self.print_Blank()
                    self.game.is_conversation = False
                    if self.end:
                        self.end = False
                        self.game.playing = False

    # 選項控制 要想一下怎麼跟checklist串聯
    def selection(self, choice):
        if self.wait_for_select:
            if choice == 1:
                if self.selection_counter == 0 or self.selection_counter == 1:
                    self.game.money += 100
                elif self.selection_counter == 2:
                    self.phase_forward()
                elif self.selection_counter == 3:
                    self.end = True
                elif self.selection_counter == 4:
                    self.game.clue_check += 1
                    self.phase_forward()
                    self.game.start_count()
                    self.game.create_sandbag_detect()
                elif self.selection_counter == 5:
                    pass
                elif self.selection_counter == 6:
                    if self.win_type == 1:
                        self.phase_3_checklist[6] = True
                        self.game.item_bag[4] -= 1
                        self.game.create_windows_pasted1()
                    else:
                        self.phase_3_checklist[7] = True
                        self.game.item_bag[4] -= 1
                        self.game.create_windows_pasted2()

                elif self.selection_counter == 7:
                    if self.phase_3_checklist[8]:
                        self.phase_3_checklist[9] = True
                        self.game.create_sandbags()
                    else:
                        self.selection_counter += 0.5
                    print('sandbag')
                    # switch sandbag
                self.now_dialog = answerGroup[int(self.selection_counter * 2)]
            elif choice == 2:
                self.now_dialog = answerGroup[self.selection_counter * 2 + 1]
            else:
                print('哭阿')
            self.wait_for_select = False
            self.counter = 0
            self.selection_counter += 1
            self.print_dialog(self.now_dialog[self.counter])
######################密密碼#######################################################
        elif self.wait_password:
            self.password = self.password+str(choice)
            print(self.password)
            self.game.screen.blit(self.font.render(self.password, True, (255, 255, 255)),
                                  (580, 650))
    #勝利條件
    def check_win(self):
        if self.phase_3_checklist[6] and self.phase_3_checklist[7] and self.phase_3_checklist[9]:
            self.game.screen.blit(self.font.render('**恭喜你成功在這次颱風中存活下來**', True, (255, 255, 255)),
                                  (580, 650))
            return True
        else:
            return False
