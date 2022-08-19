
WIN_WIDTH, WIN_HEIGHT =1280, 800

PLAYER_SPEED = 2

TILE_SIZE = 32
TILESIZE = 32

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLUE_1 = '#C4E1FF'
BLUE_2 = '#2894FF'

GROUND_LAYER = 1
BLOCK_LAYER = 2
PLAYER_LAYER = 5

blood_x = 0
blood_y = 640

#商店價錢:

NOODLE_PRICE = 100
TAPE_PRICE = 100
WATER_PRICE = 50
TOY_PRICE =100
COLA_PRICE =80

tilemap_0 = [
    'B.......................................',
    '..........................H.............',
    '........................................',
    '....S...................................',
    '........................................',
    '........................................',
    '.....////................../////........',
    '..../OOO//................/OdddO/........',
    '..../___/....$............/OOOOO/........',
    '..../OOO/................./OOOOO/...R...1',
    '..../OOO/................../////.....111',
    '..../OOO///////////////////////////01111',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO1111',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOr11111',
    '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOr11111',
    '....//////////////////////////////......',
    '........P...../OO/......................',
    '............../OO/......................',
    '..............///.......................',
    '////////////////////////////////////////',


]

tilemap_house = [
    'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
    'wb.....s..w.......V......T..wb......s..w',
    'w....D....w.................w..........w',
    'w.........w.................w..........w',
    'w.........w.................w..........w',
    'w.........w.................w..........w',
    'W.........w....l..~...C.....w......3...w',
    'w.........w.................w..........w',
    'w......................................w',
    'W......................................W',
    'w......................................w',
    'w.........w.................wwwwwww....w',
    'w.........w.................wD.........w',
    'w.........w.................w..........w',
    'w.........w.................wT.........w',
    'w....T....w.................w..........w',
    'w.........w.................w..........w',
    'w.........w.................w..........w',
    'w.........w.................w..........w',
    'wwwwwwwwwwwwwwwww#####wwwwwwwwwwwwwwwwww',

]

tilemap_river = [
    '+++t+++++++++++qqqqqqqqqqqqqqccccccccccc',
    '+++++t++++++qqq+++++++++++++qcc-cccccccc',
    '++q++q+++qqq++++++++++++++++qcccccc-cccc',
    '+q+qq+qqq++++++++++++++++++qccccc-cccccc',
    'q++++++++++++++++++++++++Aqccccc-ccccccc',
    'q+++++++++++++++++++++++AAqccc-ccccccccc',
    'q++++++++++++++++++++++AAAqccccccc-ccccc',
    'q+++++++++++++++++++++AAAqcccc-ccccccccc',
    'q+++++++++++t++++++++AAAAqcccccccccccccc',
    '@+++++++++++++++++++AAAAAqcccccc-ccccccc',
    '@++++++++++++++++++AAAAG-cccccc-cccccccc',
    '@++++++++++++++++++AAAAA-ccccccccccccccc',
    '@+++++++++++++++++3AAAG-ccc-ccccc-cccccc',
    'q++++++++++++++++++AAAqcccc-ccccccccccc-',
    'q++++++++++++++++++AAAAqcccccc-cc-cccccc',
    'q++++++++t+++++++++++AAAqccccccccccccccc',
    'q+++++++++++++++++++++AAqc-ccc-ccc-ccccc',
    'q+++++++++++++++++++++Aqccc-cccccccccccc',
    'q+++++++++++++++++++++qccccccc-ccccccc-c',
    'qqqqqqqqqqqqqqqqqqqqqqqqcccccccccccccccc',

]

KING_PATH = []
