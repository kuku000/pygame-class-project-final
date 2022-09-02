# phase 0
#######################################################################
# 進入建築物前其他建築物
phase0_hint = ['臭小子!!!沒禮貌，先去跟長老打招呼啦!!!']
# 長老對話:
king_phase0 = ['長老:俊男，終於回來啦!', '你看看這幾年沒回家，部落都變了', '我來跟你介紹一下',
               "右邊的是新開的雜貨店，沒賣什麼，不過有賣泡麵，統聯肉燥", '我:(.....統聯?)',
               '長老:再來是你右邊的那間木屋，是你今天要住的地方', '你的表弟也住在裡面', "最後就是$#@$@$@#河",
               "你表哥在那可以去跟他打聲招呼", '好了不說了去晃晃吧']
# 長老垃圾話
king_junk_phase0 = ['長老:#@#@#@#', '我:轉眼就喝醉了']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~第一階段河流
# 河流哥
river_man_phase1 = ['我:嘿!表哥好酒不見餒', '表哥:ㄟ俊男餒，可惜身邊沒帶美女', "交女朋友沒", 'selections']

river_man_selection0_phase1 = ['1.有', '2.沒有']

# 1.有
river_man_answer0_phase1 = ['表哥:很棒呦，給你吉霸摳', '讓你回去帶你女朋友吃好料', 'selections']
river_man_selection1_phase1 = ["1.100塊不夠啊", '2.謝謝表哥!']
# 1.
river_man_answer2_phase1 = ['表哥:好啦不要說我小氣:再給你100塊', '我:謝啦(......小氣)',
                            '你等等回去木屋有一台新電視，畫質不錯可以看看']
# 2.
river_man_answer3_phase1 = ['表哥:不客氣!!', '你等等回去木屋有一台新電視，畫質不錯可以看看']

# 2.沒有
river_man_answer1_phase1 = ['可惜了長那麼蟀', '好啦', '你等等回去木屋有一台新電視，畫質不錯可以看看']

# 河流哥垃圾話:
river_man_junk_phase1 = ['我跟你說', '比例海靈頓超帥']

# 黃金:
gold_phase1 = ['我:有黃金', '賺到100塊']
# 垃圾話
gold_junk_phase1 = ['不能拿瞜', '不能貪心']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~第一階段 房間
# 電視
TV_phase1 = ['我:好新電漿的電視(哪裡怪怪的)', "而且怎麼只有兩個電視台", 'selections']
TV_selections0_phase1 = ["1.山力中添新聞台", "2.NoNo長壽台"]

["1.山力中添新聞台", "NoNo長壽台"]
# 1.觸發下一階段(第二階段)
TV_answer0_phase1 = ['颱風警報!!!', '**裴洛西颱風來襲**', '請大家做好防颱準備', '記得準備*膠帶貼窗戶*以及*堆沙包在家門口*',
                     '我:我是不是該去通知一下表哥', '颱風來了在河邊很危險', '順便再去買點物資!!']
# 2.返回
TV_answer1_phase1 = ['誰的骨盆最端正', '我的骨盆最端正']
# 之後不管什麼時候點電視都是一樣的台詞


# 兩個窗戶都一樣
windows_phase1 = ['我:窗外真美', '@@##但是窗角有鳥屎!!!']

# 室友(表弟)
room_man_phase1 = ['表弟:好久不見', '你有去看那台超新的電視嗎!!!', "長老說那個是電漿的電視ㄟ", '摸螢幕還會有觸電的感覺']

# 物資箱
box_phase1 = ["一個看起來很有用的箱子"]

# ~~~~~~~~~~~~~~~~~~~~~~~~~第二階段

# 長老
king_phase2 = ['長老:@!#$$', '我:還在醉?', '長老:沒醉!!給你100塊買零食']
# 垃圾話
king_junk_phase2 = ["長老:@E@#@#ZZzzz....."]

# ~~~~~~~~~~~~~河邊(第二階段)
# 河流哥
river_man_phase2 = ['我:表哥!!颱風要來了快回家!待河邊不安全', '表哥:真假!! 難怪風變大了', "謝謝你提醒我",
                    '這個給你!長老說好像是物資箱的密碼提示', '我:長老好無聊，直接給密碼不就得了',
                    "表哥:你也知道長老最喜歡玩這種*猜謎遊戲*", "**獲得線索紙1**(線索紙1/2)", "表哥:你回去照顧一下你表弟!!",
                    '別看他那壯碩的身材',
                    "每次颱風來他都超級害怕", "多陪他聊聊天轉移他的注意力"]  # checklist_phase2[2] = True
# 垃圾話
river_man_junk_phase2 = ["表哥:如果你不想玩這個遊戲也是可以直接去問長老密碼", "我:他醉了..."]

# 黃金
gold_phase2 = ['黃金', "selections"]
gold_selections0_phase2 = ["1.撿", "2.不撿"]
gold_answer0_phase2 = ["我:幹.....表哥救我!!!", "**貪心是魔鬼，颱風天記得遠離溪水，以免發生危險**"]
gold_answer1_phase2 = ["颱風來了還是不要離河邊太近好了"]
# 1.死亡
["我:幹.....表哥救我!!!", "**貪心是魔鬼，颱風天記得遠離溪水，以免發生危險**"]
# 2.
["颱風來了還是不要離河邊太近好了"]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~找完表哥後的房間 #if checklist_phase2[2]:
# 室友(表弟)

room_man_phase2 = ["我:我回來了!!!裴洛西要來了你知道嗎", "表弟:知道呀聽說是強颱",
                   "我超害怕，你有準備好物資嗎(膠帶*有兩個窗戶*、食物...)", 'selections']
room_man_selections0_phase2 = ["1.有", "2.沒有"]
room_man_junk_phase2 = ["(先找表哥再說)"]
room_man_answer0_phase2 = ["表弟:這個給你", "**獲得線索紙2**", "**可以點擊鍵盤上的H鍵來查看線索紙1、2**",
                           "表弟:長老說這是打開物資箱密碼的線索紙", "在這種緊要關頭還要解長老的謎題...嗳"]
room_man_answer1_phase2 = ['(再檢查一下好了)']
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.有 觸發地三階段(計時開始，門上鎖 變成觸發要件)

room_man_phase3 = ["我好害怕，還是你去問長老密碼", "我:他醉了QQ", "selections"]
room_man_selecitons0_phase3 = ['1.交給我(我有能力解出來)', '2.ㄟ我盡量(會給提示)']
room_man_answer0_phase3 = ['(超簡單的 應該解得出來)']
room_man_answer1_phase3 = ['*山神護體*密碼是54XX', 'disconnect...哇收訊不太好', '只聽一半']
# 表弟垃圾話
room_man_junk_phase3 = ["表弟:哥 保護我 我好怕"]

# 物資箱:
# 在此之前都是跟一開始一樣的對話
# 出發第三階段後
box_phase3 = ["我:我想到了密碼應該是", "密碼:"]
# 這時要輸入密碼 輸入正確 獲得 沙包 失敗返回 (密碼:5478)
# 正確:
box_answer0_phase3 = ["我:打開了", "**獲得沙包**", '拿去堆大門前面']
# 失敗:返回
box_answer1_phase3 = ["我:哇!錯了"]

# 窗戶處發第三階段前與地一段一樣
# 觸發第三階段後，兩個窗戶都一樣:
windows_phase3 = ['我:來貼個窗戶', 'selections']
windows_selection0_phase3 = ["1.貼", "2.不貼"]
# 1.觸發完成要件之一(共有兩個窗戶)
window_answer0_phase3 = ["我:貼的真不錯"]
# 2.返回
window_answer1_phase3 = ["(...去檢查其他地方看看)"]
# 窗戶垃圾話
windows_junk_phase3 = ["我:美麗的窗戶，終究會留下殘膠"]
#窗戶垃圾話2 沒膠帶
windows_junk_lose = ["沒膠帶，沒交代","加油你要掛了"]
# 碰到門觸發對話
door_phase3 = ['堆沙包?', 'selections']
door_selections_phase3 = ['1.好', '2.不好']
# 1.好 觸發完成要件之一
door_answer0_phase3 = ['我:搞定']
# 2.不好 返回
door_answer1_phase3 = ["(...去檢查其他地方看看)"]
# 偵測:三個要件都達成:贏

# 時間到 或沒體力 輸

# Groups of the selection and answer
selectionsGroup = [river_man_selection0_phase1, river_man_selection1_phase1, TV_selections0_phase1,
                   gold_selections0_phase2, room_man_selections0_phase2, room_man_selecitons0_phase3,
                   windows_selection0_phase3, door_selections_phase3]
answerGroup = [river_man_answer0_phase1, river_man_answer1_phase1, river_man_answer2_phase1, river_man_answer3_phase1,
               TV_answer0_phase1, TV_answer1_phase1, gold_answer0_phase2, gold_answer1_phase2, room_man_answer0_phase2,
               room_man_answer1_phase2, room_man_answer0_phase3, room_man_answer1_phase3, window_answer0_phase3,
               window_answer1_phase3, door_answer0_phase3, door_answer1_phase3]
