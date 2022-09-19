import pygame, random
import constants as C

class Enemy:
    def __init__(self, row, col, enemy_image, theta, attack_thershold, health=0, strength=0, speed=0):
        self.row = row
        self.col = col
        self.row_pos = -1000
        self.col_pos = -1000
        self.enemy_image = pygame.transform.scale(pygame.image.load(enemy_image), (C.BLOCK_WIDTH, C.BLOCK_HEIGHT))
        self.theta = theta
        self.attack_thershold = attack_thershold
        self.aggravated = 0
        self.health = health
        self.strength = strength
        self.speed = speed
        self.last_attack = pygame.time.get_ticks()

    #Calculates how close player is to self, sets aggravated state to true if true, else sets to false
    def enemy_detect(self, player_row, player_col):
        dist_to_player = abs(player_row - self.row) + abs(player_col - self.col)
        if dist_to_player <= self.attack_thershold:
            self.aggravated = True
        else:
            self.aggravated = False
    
    #Checks to see if enemy can move before initating move
        #Return Code:
            #0 = False, can not move
            #1 = True, can move
    def enemy_movement_check(self, tile):
        if tile.type == "M" or tile.type == "W":
            return 0
        return 1

    #Checks to see if enemy is in temp_grid and sets real display pos if so, else sets off screen
    def enemy_display_check(self, temp_grid):
        row_spot = 0
        for row in temp_grid:
            col_spot = 0
            for tile in row:
                if tile.row == self.row and tile.col == self.col:
                    self.row_pos = row_spot * C.BLOCK_HEIGHT
                    self.col_pos = col_spot * C.BLOCK_WIDTH
                    return 1
                else:
                    self.row_pos = -1000
                    self.col_pos = -1000
                col_spot += 1
            row_spot += 1
   
    def enemy_draw(self, screen):
        screen.blit(pygame.transform.rotate(self.enemy_image, self.theta), (self.col_pos, self.row_pos))

class GruntEnemy(Enemy):
    #First checks if self is in aggravated state. If True, pursues player, if false, moves randomly
    def enemy_move(self, move_roll, player_row=0, player_col=0, map_grid=0):
        #Movement Code:
            #1 = Left
            #2 = Right
            #3 = Up
            #4 = Down
        if self.aggravated == True:
            row_dist = player_row - self.row
            col_dist = player_col - self.col
            #Option 1
            if row_dist < 0 and col_dist > 0:
                if move_roll % 2 == 0:
                    self.theta = 0
                    if self.enemy_movement_check(map_grid[self.row - 2][self.col - 1]) == 1:
                        self.row -= 1
                else:
                    self.theta = 270
                    if self.enemy_movement_check(map_grid[self.row - 1][self.col]) == 1:
                        self.col += 1
            #Option 2
            elif row_dist == 0 and col_dist > 0:
                self.theta = 270
                if self.enemy_movement_check(map_grid[self.row - 1][self.col]) == 1:
                    self.col += 1
            #Option 3
            elif row_dist > 0 and col_dist > 0:
                if move_roll % 2 == 0:
                    self.theta = 180
                    if self.enemy_movement_check(map_grid[self.row][self.col - 1]) == 1:
                        self.row += 1
                else:
                    self.theta = 270
                    if self.enemy_movement_check(map_grid[self.row - 1][self.col]) == 1:
                        self.col += 1
            #Option 4
            elif row_dist > 0 and col_dist == 0:
                self.theta = 180
                if self.enemy_movement_check(map_grid[self.row][self.col - 1]) == 1:
                    self.row += 1
            #Option 5
            elif row_dist > 0 and col_dist < 0:
                if move_roll % 2 == 0:
                    self.theta = 180
                    if self.enemy_movement_check(map_grid[self.row][self.col - 1]) == 1:
                        self.row += 1
                else:
                    self.theta = 90
                    if self.enemy_movement_check(map_grid[self.row - 1][self.col - 2]) == 1:
                        self.col -= 1
            #Option 6
            elif row_dist == 0 and col_dist < 0:
                self.theta = 90
                if self.enemy_movement_check(map_grid[self.row - 1][self.col - 2]) == 1:
                    self.col -= 1
            #Option 7
            elif row_dist < 0 and col_dist < 0:
                if move_roll % 2 == 0:
                    self.theta = 0
                    if self.enemy_movement_check(map_grid[self.row - 2][self.col - 1]) == 1:
                        self.row -= 1
                else:
                    self.theta = 90
                    if self.enemy_movement_check(map_grid[self.row - 1][self.col - 2]) == 1:
                        self.col -= 1
            #Option 8
            elif row_dist < 0 and col_dist == 0:
                self.theta = 0
                if self.enemy_movement_check(map_grid[self.row - 2][self.col - 1]) == 1:
                    self.row -= 1
        else:
            if move_roll == 1:
                self.col -= 1
            elif move_roll == 2:
                self.col += 1
            elif move_roll == 3:
                self.row -= 1
            elif move_roll == 4:
                self.row += 1

    #Enemy Attack - Check to see if speed criteria is met. If so, checks to see if player in range, if in range, processes attack and initates animation
    def enemy_attack(self, active_enemies, player_character, enemy_attack_particle, screen, game_map, temp_grid, shop_menu_navigator_active):
        if self.theta == 0 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            if (player_character.row == self.row and player_character.col == self.col) or (player_character.row == self.row - 1 and player_character.col == self.col):
                #Attack animation - Make sure shop isn't open
                if not(shop_menu_navigator_active):
                    duration = 15
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        player_character.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.line(screen, (255, 0, 43), (player_character.col_pos, player_character.row_pos), (player_character.col_pos + C.BLOCK_WIDTH, player_character.row_pos + C.BLOCK_HEIGHT), 2)
                        enemy_attack_particle.create_particles(player_character.col_pos + (0.5 * C.BLOCK_WIDTH), player_character.row_pos + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-6, 6), random.randint(-6, 6), 1, (255, 0, 43))
                        enemy_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    enemy_attack_particle.particles = []
                #Process enemy attack
                self.last_attack = pygame.time.get_ticks()
                player_character.health -= self.strength
        if self.theta == 90 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            if (player_character.row == self.row and player_character.col == self.col) or (player_character.row == self.row and player_character.col == self.col - 1):
                #Attack animation - Make sure shop isn't open
                if not(shop_menu_navigator_active):
                    duration = 15
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        player_character.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.line(screen, (255, 0, 43), (player_character.col_pos, player_character.row_pos), (player_character.col_pos + C.BLOCK_WIDTH, player_character.row_pos + C.BLOCK_HEIGHT), 2)
                        enemy_attack_particle.create_particles(player_character.col_pos + (0.5 * C.BLOCK_WIDTH), player_character.row_pos + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-6, 6), random.randint(-6, 6), 1, (255, 0, 43))
                        enemy_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    enemy_attack_particle.particles = []
                #Process enemy attack
                self.last_attack = pygame.time.get_ticks()
                player_character.health -= (self.strength - player_character.armour)
        if self.theta == 180 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            if (player_character.row == self.row and player_character.col == self.col) or (player_character.row == self.row + 1 and player_character.col == self.col):
                #Attack animation - Make sure shop isn't open
                if not(shop_menu_navigator_active):
                    duration = 15
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        player_character.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.line(screen, (255, 0, 43), (player_character.col_pos, player_character.row_pos), (player_character.col_pos + C.BLOCK_WIDTH, player_character.row_pos + C.BLOCK_HEIGHT), 2)
                        enemy_attack_particle.create_particles(player_character.col_pos + (0.5 * C.BLOCK_WIDTH), player_character.row_pos + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-6, 6), random.randint(-6, 6), 1, (255, 0, 43))
                        enemy_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    enemy_attack_particle.particles = []
                #Process enemy attack
                self.last_attack = pygame.time.get_ticks()
                player_character.health -= self.strength
        if self.theta == 0 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            if (player_character.row == self.row and player_character.col == self.col) or (player_character.row == self.row and player_character.col == self.col + 1):
                #Attack animation - Make sure shop isn't open
                if not(shop_menu_navigator_active):
                    duration = 15
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        player_character.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.line(screen, (255, 0, 43), (player_character.col_pos, player_character.row_pos), (player_character.col_pos + C.BLOCK_WIDTH, player_character.row_pos + C.BLOCK_HEIGHT), 2)
                        enemy_attack_particle.create_particles(player_character.col_pos + (0.5 * C.BLOCK_WIDTH), player_character.row_pos + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-6, 6), random.randint(-6, 6), 1, (255, 0, 43))
                        enemy_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    enemy_attack_particle.particles = []
                #Process enemy attack
                self.last_attack = pygame.time.get_ticks()
                player_character.health -= self.strength

class Levels:
    def __init__(self):
        self.level = 0
        self.level_duration = 60000
        self.level_previous = pygame.time.get_ticks()
        self.level_countdown  = pygame.time.get_ticks() - self.level_previous
        self.level_countdown_actual = round(self.level_countdown / 1000)
        self.active_enemies = []
        self.num_enemies_max = 3 
        self.enemy_spawn_prob = 1 
        self.enemy_grunt_prob = 100
    
    def level_timer_check_update(self):
        self.level_countdown  = pygame.time.get_ticks() - self.level_previous
        self.level_countdown_actual = round((60000 - self.level_countdown) / 1000)
        if self.level_countdown >= self.level_duration:
            self.level += 1
            self.level_previous = pygame.time.get_ticks()
            self.num_enemies_max = 3 + self.level * 2
            self.enemy_spawn_prob = 1 + round(self.level * 0.1)
    
    def enemy_spawn(self, game_map):
         #Check to see if spawning more enemies is possible, chance to spawn enemy in random spot if true
        if len(self.active_enemies) < self.num_enemies_max:
            spawn_roll = random.randrange(1, 101)
            if spawn_roll in range(1, self.enemy_spawn_prob + 1):
                type_roll = random.randrange(1, 101)
                if type_roll in range (1, self.enemy_grunt_prob + 1):
                    rand_row = random.randrange(2, C.TOTAL_BLOCKS_HIGH)
                    rand_col = random.randrange(2, C.TOTAL_BLOCKS_WIDE)
                    #Safeguard to make sure enemies don't spawn on forbidden tile
                    if game_map.map_grid[rand_row - 1][rand_col - 1].type == "M" or game_map.map_grid[rand_row - 1][rand_col - 1].type == "W":
                        pass
                    else:
                        new_enemy_grunt = GruntEnemy(rand_row, rand_col, C.ENEMY_IMAGE_TITLE_GRUNT, 0, 5, 15 + self.level, 5 + self.level * 0.5, 2000 + 250 * self.level * 0.5)
                        self.active_enemies.append(new_enemy_grunt)
                #Add other types of enemies here if needed
    