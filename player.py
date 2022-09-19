import pygame, random
import constants as C

class Player:
    def __init__(self, row, col, row_pos, col_pos, player_image, theta, health=100, strength=5, speed=1500):
        self.row = row
        self.col = col
        self.row_pos = row_pos
        self.col_pos = col_pos
        self.player_image = pygame.transform.scale(pygame.image.load(player_image), (C.BLOCK_WIDTH, C.BLOCK_HEIGHT))
        self.theta = theta
        self.health = health
        self.strength = strength
        self.speed = speed
        self.last_attack = pygame.time.get_ticks()
        self.armour = 0
        self.health_regeneration = 0.01
        self.equipped_inventory = [None, None, None, None, None, None, None]
        self.inventory = []
        self.coins = 100
        self.player_statuses = []

    #Checks to see if player can move before initating move
        #Return Code:
            #0 = False, can not move
            #1 = True, can move
    def player_movement_check(self, tile):
        if tile.type == "M" or tile.type == "W":
            return 0
        return 1

    #Update player location, both coords and actual pos
        #Movement Code:
            #1 = Left
            #2 = Right
            #3 = Up
            #4 = Down
    def player_move(self, direction):
        if direction == 1:
            self.col -= 1
            if self.col <= (C.NUMBER_OF_BLOCKS_WIDE / 2) or self.col >= ((C.TOTAL_BLOCKS_WIDE - (C.NUMBER_OF_BLOCKS_WIDE / 2)) + 1):
                self.col_pos -= C.PLAYER_MOVEMENT_DISTANCE_X
        elif direction == 2:
            self.col += 1
            if self.col <= ((C.NUMBER_OF_BLOCKS_WIDE / 2) + 1) or self.col >= ((C.TOTAL_BLOCKS_WIDE - (C.NUMBER_OF_BLOCKS_WIDE / 2)) + 2):
                self.col_pos += C.PLAYER_MOVEMENT_DISTANCE_X
        elif direction == 3:
            self.row -= 1
            if self.row <= (C.NUMBER_OF_BLOCKS_HIGH / 2) or self.row >= ((C.TOTAL_BLOCKS_HIGH - (C.NUMBER_OF_BLOCKS_HIGH / 2)) + 1):
                self.row_pos -= C.PLAYER_MOVEMENT_DISTANCE_Y
        elif direction == 4:
            self.row += 1
            if self.row <= ((C.NUMBER_OF_BLOCKS_HIGH / 2) + 1) or self.row >= ((C.TOTAL_BLOCKS_HIGH - (C.NUMBER_OF_BLOCKS_HIGH / 2)) + 2):
                self.row_pos += C.PLAYER_MOVEMENT_DISTANCE_Y      

    #Manage Player attacks. Check to see if speed critera is met. If so, check active_enemies for enemy in range, if in range, initate attack process + animation
    def player_attack(self, active_enemies, player_attack_particle, screen, game_map, temp_grid):
        if self.speed >= 0:
            attack_delay = self.speed
        else:
            attack_delay = 0
        if self.theta == 0 and (pygame.time.get_ticks() - self.last_attack) > attack_delay:
            for active_enemy in active_enemies:
                if (active_enemy.row == self.row and active_enemy.col == self.col) or (active_enemy.row == self.row - 1 and active_enemy.col == self.col): 
                    #Attack Animation
                    duration = 20
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        self.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.arc(screen, (51, 255, 255), [self.col_pos, self.row_pos - (0.25 * C.BLOCK_HEIGHT), C.BLOCK_WIDTH, C.BLOCK_HEIGHT], (3.14 / 6), (5 * 3.14 / 6), 2)
                        player_attack_particle.create_particles(self.col_pos + (0.5 * C.BLOCK_WIDTH), self.row_pos, 5, random.randint(-7, 7), random.randint(-7, 7), 1, (51, 255, 255))
                        player_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    player_attack_particle.particles = []
                    #Process Player Attack
                    active_enemy.health -= self.strength
                    self.last_attack = pygame.time.get_ticks()
        elif self.theta == 90 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            for active_enemy in active_enemies:
                if (active_enemy.row == self.row and active_enemy.col == self.col) or (active_enemy.row == self.row and active_enemy.col == self.col - 1): 
                    #Attack Animation
                    duration = 20
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        self.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.arc(screen, (51, 255, 255), [self.col_pos - (0.25 * C.BLOCK_WIDTH), self.row_pos, C.BLOCK_WIDTH, C.BLOCK_HEIGHT], (2 * 3.14 / 3), (4 * 3.14 / 3), 2)
                        player_attack_particle.create_particles(self.col_pos, self.row_pos  + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-7, 7), random.randint(-7, 7), 1, (51, 255, 255))
                        player_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    player_attack_particle.particles = []
                    #Process Player Attack
                    active_enemy.health -= self.strength
                    self.last_attack = pygame.time.get_ticks()
        elif self.theta == 180 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            for active_enemy in active_enemies:
                if (active_enemy.row == self.row and active_enemy.col == self.col) or (active_enemy.row == self.row + 1 and active_enemy.col == self.col): 
                    #Attack Animation
                    duration = 20
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        self.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.arc(screen, (51, 255, 255), [self.col_pos, self.row_pos + (0.25 * C.BLOCK_HEIGHT), C.BLOCK_WIDTH, C.BLOCK_HEIGHT], (7 * 3.14 / 6), (11 * 3.14 / 6), 2)
                        player_attack_particle.create_particles(self.col_pos + (0.5 * C.BLOCK_WIDTH), self.row_pos + (1 * C.BLOCK_HEIGHT), 5, random.randint(-7, 7), random.randint(-7, 7), 1, (51, 255, 255))
                        player_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    player_attack_particle.particles = []
                    #Process Player Attack
                    active_enemy.health -= self.strength
                    self.last_attack = pygame.time.get_ticks()
        elif self.theta == 270 and (pygame.time.get_ticks() - self.last_attack) > self.speed:
            for active_enemy in active_enemies:
                if (active_enemy.row == self.row and active_enemy.col == self.col) or (active_enemy.row == self.row and active_enemy.col == self.col + 1): 
                    #Attack Animation
                    duration = 20
                    while duration > 0:
                        game_map.map_draw(screen, temp_grid)
                        self.player_draw(screen)
                        for enemy in active_enemies:
                            enemy.enemy_draw(screen)
                        pygame.draw.arc(screen, (51, 255, 255), [self.col_pos + (0.25 * C.BLOCK_WIDTH), self.row_pos, C.BLOCK_WIDTH, C.BLOCK_HEIGHT], (5 * 3.14 / 3), (3.14 / 3), 2)
                        player_attack_particle.create_particles(self.col_pos + (1 * C.BLOCK_WIDTH), self.row_pos + (0.5 * C.BLOCK_HEIGHT), 5, random.randint(-7, 7), random.randint(-7, 7), 1, (51, 255, 255))
                        player_attack_particle.animate_particles()
                        pygame.display.update()
                        duration -= 1
                    player_attack_particle.particles = []
                    #Process Player Attack
                    active_enemy.health -= self.strength
                    self.last_attack = pygame.time.get_ticks()

    def check_player_statuses(self):
        if self.player_statuses:
            #Check to see if still active, remove effect and delete if not
            for i in range(len(self.player_statuses) - 1, -1, -1):
                if (pygame.time.get_ticks() - self.player_statuses[i][3]) > (self.player_statuses[i][1] * 1000 * 60):
                    if self.player_statuses[i][2] == (5, 2):
                        self.strength -= self.player_statuses[i][0]
                        del self.player_statuses[i]
                    elif self.player_statuses[i][2] == (5, 3):
                        self.speed += self.player_statuses[i][0] * 1000
                        del self.player_statuses[i]

    #Draws the player's character on the screen
    def player_draw(self, screen):
        screen.blit(pygame.transform.rotate(self.player_image, self.theta), (self.col_pos, self.row_pos))

