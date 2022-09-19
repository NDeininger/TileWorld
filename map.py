import pygame
import constants as C

class MapTile:
    def __init__(self, type, row, col):
        self.type = type
        self.row = row
        self.col = col
    
    def get_tile(self):
        tile_color = C.TILE_DEFAULT_COLOR
        if self.type == "G":
            tile_color = C.GRASS_GREEN
        elif self.type == "M":
            tile_color = C.MOUNTAIN_BROWN
        elif self.type == "W":
            tile_color = C.WATER_BLUE
        elif self.type == "S":
            tile_color = C.SNOW_WHITE
        return(tile_color)
        
class GameMap:
    map_data = []
    map_grid = [] 
    
    #Read map_file, store information into map_data
    with open(C.MAP_FILE_TITLE) as map_file:
        for line in map_file:
            map_data.append(line[:-1])  

    #Take map_data, create a MapTile class for each tile, store into map_grid in grid form
    row_pos = 1
    for row in map_data:
        temp_row = []
        col_pos = 1
        for col in row:
            newtile = MapTile(col,row_pos,col_pos)
            temp_row.append(newtile)
            col_pos += 1
        map_grid.append(temp_row)
        row_pos += 1
        col_pos = 1   

    def get_temp_grid(self, player_col, player_row):
        temp_grid_row = []
        temp_grid = []
        #Set initial grid parameters, centered around player
        row_top = int(player_row - (C.NUMBER_OF_BLOCKS_HIGH / 2) - 1)
        row_bottom = int(player_row + (C.NUMBER_OF_BLOCKS_HIGH / 2) - 1)
        col_left = int(player_col - (C.NUMBER_OF_BLOCKS_WIDE / 2) - 1)
        col_right = int(player_col + (C.NUMBER_OF_BLOCKS_WIDE / 2) - 1)
        #Check parameters for border collison, adjust if needed
        if row_top < 1:
            excess = 0 - row_top
            row_top += excess
            row_bottom += excess
        if row_bottom > C.TOTAL_BLOCKS_HIGH:
            excess = row_bottom - C.TOTAL_BLOCKS_HIGH
            row_bottom -= excess
            row_top -= excess
        if col_left < 1:
            excess = 0 - col_left
            col_left += excess
            col_right += excess
        if col_right > C.TOTAL_BLOCKS_WIDE:
            excess = col_right - C.TOTAL_BLOCKS_WIDE
            col_right -= excess
            col_left -= excess
        #Retrieve 2D list of grid points using parameters
        for temp_row in range(row_top, row_bottom):
            temp_grid_row = []
            for temp_col in range(col_left, col_right):
                temp_grid_row.append(self.map_grid[temp_row][temp_col])
            temp_grid.append(temp_grid_row)
        return(temp_grid)

    def map_draw(self, screen, temp_grid):
        #Use 2D temp_grid to draw anchored display on screen
        for row in range(0, C.NUMBER_OF_BLOCKS_HIGH):
            for col in range(0, C.NUMBER_OF_BLOCKS_WIDE):
                rect = pygame.Rect(col * C.BLOCK_WIDTH, row * C.BLOCK_HEIGHT, C.BLOCK_WIDTH, C.BLOCK_HEIGHT)
                pygame.draw.rect(screen, temp_grid[row][col].get_tile(), rect)
                #Horizontal Grid Line
                pygame.draw.line(screen, (0,0,0), (0, row * C.BLOCK_HEIGHT), (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH, row * C.BLOCK_HEIGHT), 1)
                #Vertical Grid Line
                pygame.draw.line(screen, (0,0,0), (col * C.BLOCK_WIDTH, 0), (col * C.BLOCK_WIDTH, C.NUMBER_OF_BLOCKS_HIGH * C.BLOCK_HEIGHT), 1)
        pygame.draw.line(screen, (0,0,0), (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH, 0), (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH, C.NUMBER_OF_BLOCKS_HIGH * C.BLOCK_HEIGHT), 1)
