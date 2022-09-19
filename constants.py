from screeninfo import get_monitors

GAME_TITLE = "Tile World"
GAME_ICON = "images\game_icon.png"
MAP_FILE_TITLE = "maps\map_data_big.txt"
PLAYER_IMAGE_TITLE = "images\player.png"

MONITOR = get_monitors()
MONITOR = MONITOR[0]

#Adjust screen display to fit monitor size
if MONITOR.height < MONITOR.width:
    SCREEN_HEIGHT = MONITOR.height
    SCREEN_WIDTH = SCREEN_HEIGHT
else:
    SCREEN_WIDTH = MONITOR.width
    SCREEN_HEIGHT = SCREEN_WIDTH

#Number of blocks to be displayed on screen, Keep Equal
NUMBER_OF_BLOCKS_WIDE = 20
NUMBER_OF_BLOCKS_HIGH = 20

#Total number of map blocks
TOTAL_BLOCKS_WIDE = 50
TOTAL_BLOCKS_HIGH = 50

#Adjust block sizes to fit monitor
if MONITOR.height < MONITOR.width:
    BLOCK_HEIGHT = round(SCREEN_HEIGHT/NUMBER_OF_BLOCKS_HIGH)
    BLOCK_WIDTH = BLOCK_HEIGHT
else:
    BLOCK_WIDTH = round(SCREEN_WIDTH/NUMBER_OF_BLOCKS_WIDE)
    BLOCK_HEIGHT = BLOCK_WIDTH

PLAYER_START_X_POS = (round(NUMBER_OF_BLOCKS_WIDE / 2) * BLOCK_WIDTH) 
PLAYER_START_Y_POS = (round(NUMBER_OF_BLOCKS_HIGH / 2) * BLOCK_HEIGHT) 
PLAYER_START_X_COORD = (round(TOTAL_BLOCKS_WIDE / 2)) + 1
PLAYER_START_Y_COORD = (round(TOTAL_BLOCKS_HIGH / 2)) + 1

PLAYER_MOVEMENT_DISTANCE_X = BLOCK_WIDTH
PLAYER_MOVEMENT_DISTANCE_Y = BLOCK_HEIGHT

#Enemy Type: Grunt
ENEMY_IMAGE_TITLE_GRUNT = "images\enemy_image.png"

BACKGROUND_COLOR = (255, 0, 255)
TILE_DEFAULT_COLOR = (181, 255, 68) 
GRASS_GREEN = (0, 153, 0)
SNOW_WHITE = (255,250,250)
WATER_BLUE = (0, 0, 153)
MOUNTAIN_BROWN = (51, 25, 0)
BLACK = (0, 0, 0)
