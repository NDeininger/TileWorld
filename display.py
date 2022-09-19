import pygame
import constants as C

class PlayerStatusBar:
    def __init__(self, player_character):
        self.background_rect = pygame.Rect(C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1, 0, C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH), C.BLOCK_HEIGHT * 6 + 1)
        self.healthbar_background = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 15) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.05, C.BLOCK_HEIGHT * 0.5, (C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.1), C.BLOCK_HEIGHT * 1.5)
        self.healthbar = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 15) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.05, C.BLOCK_HEIGHT * 0.5, ((C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.1)) * (player_character.health / 100), C.BLOCK_HEIGHT * 1.5)
        self.healthbar_edge = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 15) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.05, C.BLOCK_HEIGHT * 0.5, (C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.1), C.BLOCK_HEIGHT * 1.5)
        self.statusbar_font = pygame.font.Font(None, 34)
        self.healthbarfont_surface = self.statusbar_font.render("HP", True, (224, 224, 224)) 
        self.strengthfont_surface = self.statusbar_font.render("Strength: {}".format(player_character.strength), True, (224, 224, 224))
        self.speedfont_surface = self.statusbar_font.render("Speed: {}".format(player_character.speed / 1000), True, (224, 224, 224))
        self.armourfont_surface = self.statusbar_font.render("Armour: {}".format(player_character.armour), True, (224, 224, 224))
        self.regenfont_surface = self.statusbar_font.render("Regeneration: {}".format(player_character.health_regeneration), True, (224, 224, 224))
        self.coinfont_surface = self.statusbar_font.render("Coins: {}".format(player_character.coins), True, (224, 224, 224))

    def statusbar_update(self, player_character):
        self.healthbar = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 15) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.05, C.BLOCK_HEIGHT * 0.5, ((C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH + 1) * 0.1)) * (player_character.health / 100), C.BLOCK_HEIGHT * 1.5)
        self.strengthfont_surface = self.statusbar_font.render("Strength: {}".format(player_character.strength), True, (224, 224, 224))
        self.speedfont_surface = self.statusbar_font.render("Speed: {}".format(player_character.speed / 1000), True, (224, 224, 224))
        self.armourfont_surface = self.statusbar_font.render("Armour: {}".format(player_character.armour), True, (224, 224, 224))
        self.regenfont_surface = self.statusbar_font.render("Regeneration: {}".format(player_character.health_regeneration), True, (224, 224, 224))
        self.coinfont_surface = self.statusbar_font.render("Coins: {}".format(player_character.coins), True, (224, 224, 224))

    def statusbar_display(self, screen, player_character):
        pygame.draw.rect(screen, (0,0,0), self.background_rect)
        pygame.draw.rect(screen, (160, 160, 160), self.healthbar_background)
        self.statusbar_update(player_character)
        pygame.draw.rect(screen, (255, 65, 65), self.healthbar)
        pygame.draw.rect(screen, (192, 192, 192), self.healthbar_edge, 1)
        screen.blit(self.healthbarfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.02, C.BLOCK_HEIGHT * 1.15))
        screen.blit(self.strengthfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.02, C.BLOCK_HEIGHT * 2.4))
        screen.blit(self.speedfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.02, C.BLOCK_HEIGHT * 3.4))
        screen.blit(self.armourfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.02, C.BLOCK_HEIGHT * 4.4))
        screen.blit(self.regenfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.02, C.BLOCK_HEIGHT * 5.4))
        screen.blit(self.coinfont_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.6, C.BLOCK_HEIGHT * 2.4))

class PlayerInventoryDisplay:
    def __init__(self):
        self.top_border_bar = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1, (C.BLOCK_HEIGHT * 6) + 1, C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH), (C.BLOCK_HEIGHT * 2))
        self.bottom_border_bar = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1, C.BLOCK_HEIGHT * 18, C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH), C.BLOCK_HEIGHT * 2)
        self.inventory_background = pygame.Rect((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1, C.BLOCK_HEIGHT * 8, C.MONITOR.width - (C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH), (C.BLOCK_HEIGHT * 10) + 1)
        self.equipped_item_slots = [pygame.Rect(((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * iteration, C.BLOCK_HEIGHT * 8, (C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7, C.BLOCK_HEIGHT * 2) for iteration in range(0, 7)]
        self.item_slots = [[pygame.Rect(((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * iteration, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * row * 2), (C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7, C.BLOCK_HEIGHT * 2) for iteration in range(0, 7)] for row in range(0, 4)]
        self.equipped_item_title_font = pygame.font.Font(None, 38)
        self.equipped_item_title_font_surface = self.equipped_item_title_font.render("Equipped Items", True, (224, 224, 224))
        self.equipped_item_font = pygame.font.Font(None, 22)
        self.equipped_item_weapon_font_surface = self.equipped_item_font.render("Weapon", True, (0, 0, 0))
        self.equipped_item_armour_font_surface = self.equipped_item_font.render("Armour", True, (0, 0, 0))
        self.equipped_item_shoes_font_surface = self.equipped_item_font.render("Shoes", True, (0, 0, 0))
        self.equipped_item_ring_font_surface = self.equipped_item_font.render("Ring", True, (0, 0, 0))
        self.equipped_auxillaryone_font_surface = self.equipped_item_font.render("Auxillary 1", True, (0, 0, 0))
        self.equipped_auxillarytwo_font_surface = self.equipped_item_font.render("Auxillary 2", True, (0, 0, 0))
        self.equipped_auxillarythree_font_surface = self.equipped_item_font.render("Auxillary 3", True, (0, 0, 0))
        
    def player_equipped_display(self, screen, player_equipped_inventory):
        item_index = 0
        for item in player_equipped_inventory:
            if item != None:
                screen.blit(player_equipped_inventory[item_index].item_image, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1 + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * item_index + 12, C.BLOCK_HEIGHT * 8 + 12))
            item_index += 1

    def player_inventory_display(self, screen, player_inventory):
        item_index = 0
        for row in range (0, 4):
            item_top = (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * row * 2)
            for col in range (0, 7):
                item_left = ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * col
                if item_index < len(player_inventory):
                    screen.blit(player_inventory[item_index].item_image, (item_left, item_top))
                else: 
                    return
                item_index += 1
   
    def inventory_setup_display(self, screen):
            pygame.draw.rect(screen, (128, 128, 128), self.top_border_bar)
            pygame.draw.rect(screen, (128, 128, 128), self.bottom_border_bar)
            pygame.draw.rect(screen, (64, 64, 64), self.inventory_background)
            for slot in self.equipped_item_slots:
                pygame.draw.rect(screen, (92, 225, 87), slot)
            for slot_edge in self.equipped_item_slots:
                pygame.draw.rect(screen, (0, 0, 0), slot_edge, 2)
            for row in self.item_slots:
                for slot_edge in row:
                    pygame.draw.rect(screen, (0, 0, 0), slot_edge, 1)
            screen.blit(self.equipped_item_title_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) * 0.38, C.BLOCK_HEIGHT * 7))
            screen.blit(self.equipped_item_weapon_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_item_armour_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_item_shoes_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * 2) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_item_ring_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * 3) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_auxillaryone_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * 4) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_auxillarytwo_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * 5) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))
            screen.blit(self.equipped_auxillarythree_font_surface, ((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + (((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * 6) + (C.BLOCK_WIDTH * 0.1), (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * 0.1)))

class InventoryNavigatorDisplay:
    def __init__(self):
        self.item_info_active = False
        self.del_item_active = False
        self.navigator_rect = pygame.Rect(((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7), C.BLOCK_HEIGHT * 8, (C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7, C.BLOCK_HEIGHT * 2)

    def display_nav_rect(self, screen, inventory_nav_row, inventory_nav_col):
        self.navigator_rect = pygame.Rect(((C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 8) + (C.BLOCK_HEIGHT * inventory_nav_row * 2), (C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7, C.BLOCK_HEIGHT * 2)
        pygame.draw.rect(screen, (255, 247, 0), self.navigator_rect, 1)

    def display_item_info(self, screen, display_string, inventory_nav_row, inventory_nav_col):
        self.background_rect = pygame.Rect((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row * 1), C.BLOCK_WIDTH * 5, C.BLOCK_HEIGHT * 3)
        self.background_rect_border = pygame.Rect((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row * 1), C.BLOCK_WIDTH * 5, C.BLOCK_HEIGHT * 3)
        self.item_info_font = pygame.font.Font(None, 28)
        pygame.draw.rect(screen, (32, 32, 32), self.background_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect_border, 2)
        line_count = 0
        for line in display_string:
            self.item_info_font_surface = self.item_info_font.render(line, True, (224, 224, 224))
            screen.blit(self.item_info_font_surface, ((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 5) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row + 3) + (27 * line_count)))
            line_count += 1
    
    def del_item_prompt(self, screen, inventory_nav_row, inventory_nav_col):
        self.prompt_string_font = pygame.font.Font(None, 28)
        self.prompt_string_font_surface1 = self.prompt_string_font.render("                           WARNING!", True, (224, 224, 224))
        self.prompt_string_font_surface2 = self.prompt_string_font.render("Are you sure you want to delete that item?", True, (224, 224, 224))
        self.prompt_string_font_surface3 = self.prompt_string_font.render("Enter: y/n", True, (224, 224, 224))
        self.prompt_background_rect = pygame.Rect((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 1) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row * 1), C.BLOCK_WIDTH * 7.5, C.BLOCK_HEIGHT * 1.5)
        pygame.draw.rect(screen, (32, 32, 32), self.prompt_background_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.prompt_background_rect, 2)
        screen.blit(self.prompt_string_font_surface1, ((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 5) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row + 3)))
        screen.blit(self.prompt_string_font_surface2, ((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 5) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row + 3) + (28 * 1)))
        screen.blit(self.prompt_string_font_surface3, ((((C.NUMBER_OF_BLOCKS_WIDE + 1) * C.BLOCK_WIDTH) + 5) + ((C.MONITOR.width - C.NUMBER_OF_BLOCKS_WIDE * C.BLOCK_WIDTH) / 7) * inventory_nav_col, (C.BLOCK_HEIGHT * 10) + (C.BLOCK_HEIGHT * inventory_nav_row + 3) + (27 * 2)))

class ShopDisplay:
    def __init__(self):
        self.top_rect = pygame.Rect(C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 4, C.BLOCK_WIDTH * 16 + 0.75, C.BLOCK_HEIGHT * 2)
        self.top_rect_border = pygame.Rect(C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 4, C.BLOCK_WIDTH * 16 , C.BLOCK_HEIGHT * 2)
        self.background_rect = pygame.Rect(C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 4, C.BLOCK_WIDTH * 16 + 0.75, C.BLOCK_HEIGHT * 14)
        self.background_rect_border = pygame.Rect(C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 4, C.BLOCK_WIDTH * 16, C.BLOCK_HEIGHT * 14)
        self.item_slots = [[pygame.Rect(C.BLOCK_WIDTH * 2 * col + C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 * row + C.BLOCK_HEIGHT * 6, C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2) for col in range(0, 8)] for row in range(0, 6)]
        self.header_string_font = pygame.font.Font(None, 44)
        self.header_string_font_surface = self.header_string_font.render("SHOP", True, (224, 224, 224))
    
    def display_shop(self, screen):
        pygame.draw.rect(screen, (64, 64, 64), self.background_rect)
        pygame.draw.rect(screen, (128, 128, 128), self.top_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect_border, 2)
        pygame.draw.rect(screen, (0, 0, 0), self.top_rect_border, 2)
        screen.blit(self.header_string_font_surface, (C.BLOCK_WIDTH * 9.25, C.BLOCK_HEIGHT * 4.5))
        for row in self.item_slots:
            for slot_edge in row:
                pygame.draw.rect(screen, (0, 0, 0), slot_edge, 1)

    def display_shop_items(self, screen):
        for row in range(0, 4):
            for col in range(0, 4):
                if row == 0:
                    screen.blit(pygame.image.load("images/sword.png"), (C.BLOCK_WIDTH * 2 * col + C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 * row + C.BLOCK_HEIGHT * 6))
                elif row == 1:
                    screen.blit(pygame.image.load("images/armour.png"), (C.BLOCK_WIDTH * 2 * col + C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 * row + C.BLOCK_HEIGHT * 6))
                elif row == 2:
                    screen.blit(pygame.image.load("images/shoe.png"), (C.BLOCK_WIDTH * 2 * col + C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 * row + C.BLOCK_HEIGHT * 6))
                else:
                    screen.blit(pygame.image.load("images/ring.png"), (C.BLOCK_WIDTH * 2 * col + C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 * row + C.BLOCK_HEIGHT * 6))
        screen.blit(pygame.image.load("images/potion1.png"), (C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))
        screen.blit(pygame.image.load("images/potion1.png"), (C.BLOCK_WIDTH * 4, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))
        screen.blit(pygame.image.load("images/potion2.png"), (C.BLOCK_WIDTH * 6, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))
        screen.blit(pygame.image.load("images/potion2.png"), (C.BLOCK_WIDTH * 8, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))
        screen.blit(pygame.image.load("images/potion3.png"), (C.BLOCK_WIDTH * 10, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))
        screen.blit(pygame.image.load("images/potion3.png"), (C.BLOCK_WIDTH * 12, C.BLOCK_HEIGHT * 2 + C.BLOCK_HEIGHT * 12))

class ShopNavigatorDisplay:
    def __init__(self):
        self.item_info_active = False
        self.buy_item_prompt_active = False
        self.insufficient_coins_prompt_active = False
        self.navigator_rect = pygame.Rect(C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 6, C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2)

    def display_nav_rect(self, screen, inventory_nav_row, inventory_nav_col):
        self.navigator_rect = pygame.Rect(C.BLOCK_WIDTH * 2 + inventory_nav_col * 2 * C.BLOCK_WIDTH, C.BLOCK_HEIGHT * 6 + inventory_nav_row * 2 * C.BLOCK_HEIGHT, C.BLOCK_WIDTH * 2, C.BLOCK_HEIGHT * 2)
        pygame.draw.rect(screen, (255, 247, 0), self.navigator_rect, 1)

    def display_item_info(self, screen, display_string, inventory_nav_row, inventory_nav_col):
        self.background_rect = pygame.Rect((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col) , (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row),  C.BLOCK_WIDTH * 5, C.BLOCK_HEIGHT * 3.5)
        self.background_rect_border = pygame.Rect((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col), (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row), C.BLOCK_WIDTH * 5, C.BLOCK_HEIGHT * 3.5)
        self.item_info_font = pygame.font.Font(None, 27)
        pygame.draw.rect(screen, (32, 32, 32), self.background_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect_border, 2)
        line_count = 0
        for line in display_string:
            self.item_info_font_surface = self.item_info_font.render(line, True, (224, 224, 224))
            screen.blit(self.item_info_font_surface, ((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col) + 5, (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row) + (27 * line_count) + 5))
            line_count += 1

    def buy_item_prompt(self, screen, inventory_nav_row, inventory_nav_col):
        self.background_rect = pygame.Rect((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col) , (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row),  C.BLOCK_WIDTH * 9.5, C.BLOCK_HEIGHT * 1.5)
        self.background_rect_border = pygame.Rect((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col), (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row), C.BLOCK_WIDTH * 9.5, C.BLOCK_HEIGHT * 1.5)
        self.buy_prompt_font = pygame.font.Font(None, 32)
        self.buy_prompt_surface = self.buy_prompt_font.render("Are you sure you wish to buy this item? (y/n)", True, (224, 224, 224))
        pygame.draw.rect(screen, (32, 32, 32), self.background_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect_border, 2)
        screen.blit(self.buy_prompt_surface, ((C.BLOCK_WIDTH * 3) + (C.BLOCK_WIDTH * 2 * inventory_nav_col) + 5, (C.BLOCK_HEIGHT * 7) + (C.BLOCK_HEIGHT * 2 * inventory_nav_row) + 5))

    def insufficient_coins_prompt(self, screen):
        self.background_rect = pygame.Rect(C.SCREEN_WIDTH * 0.35, C.SCREEN_HEIGHT * 0.4, C.SCREEN_WIDTH * 0.50, C.SCREEN_HEIGHT * 0.2)
        self.border_rect = pygame.Rect(C.SCREEN_WIDTH * 0.35, C.SCREEN_HEIGHT * 0.4, C.SCREEN_WIDTH * 0.50, C.SCREEN_HEIGHT * 0.2)
        self.prompt_string_font = pygame.font.Font(None, 32)
        self.prompt_string_font_surface1 = self.prompt_string_font.render("Insufficient coins to purchase this item!", True, (224, 224, 224))
        self.prompt_string_font_surface2 = self.prompt_string_font.render("Press Enter to acknowledge.", True, (224, 224, 224))
        pygame.draw.rect(screen, (32, 32, 32), self.background_rect) 
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect, 1)
        screen.blit(self.prompt_string_font_surface1, (C.SCREEN_WIDTH * 0.4, C.SCREEN_HEIGHT * 0.46))
        screen.blit(self.prompt_string_font_surface2, (C.SCREEN_WIDTH * 0.45, C.SCREEN_HEIGHT * 0.51))

class LevelDisplay:
    def __init__(self, level):
        self.level_display_font = pygame.font.Font(None, 36)
        self.countdown_display_font = pygame.font.Font(None, 36)
        self.level_display_font_surface = self.level_display_font.render("Level: {}".format(level.level), True, (224, 224, 224))
        self.countdown_display_font_surface = self.countdown_display_font.render("Time Until Next Level: {}".format(level.level_countdown_actual), True, (224, 224, 224))

    def level_display_update(self, level):
        self.level_display_font_surface = self.level_display_font.render("Level: {}".format(level.level), True, (224, 224, 224))
        self.countdown_display_font_surface = self.countdown_display_font.render("Time Until Next Level: {}".format(level.level_countdown_actual), True, (224, 224, 224))
    
    def level_countdown_display(self, screen):
        screen.blit(self.level_display_font_surface, (C.MONITOR.width * 0.65, C.MONITOR.height * 0.93))
        screen.blit(self.countdown_display_font_surface, (C.MONITOR.width * 0.75, C.MONITOR.height * 0.93))

class QuitPrompt:
    def __init__(self):
        self.background_rect = pygame.Rect(C.SCREEN_WIDTH * 0.35, C.SCREEN_HEIGHT * 0.4, C.SCREEN_WIDTH * 0.50, C.SCREEN_HEIGHT * 0.2)
        self.border_rect = pygame.Rect(C.SCREEN_WIDTH * 0.35, C.SCREEN_HEIGHT * 0.4, C.SCREEN_WIDTH * 0.50, C.SCREEN_HEIGHT * 0.2)
        self.prompt_string_font = pygame.font.Font(None, 32)
        self.prompt_string_font_surface = self.prompt_string_font.render("Are you sure you want to end game session? (y/n)", True, (224, 224, 224))
    
    def quit_prompt_display(self, screen):
        pygame.draw.rect(screen, (32, 32, 32), self.background_rect) 
        pygame.draw.rect(screen, (0, 0, 0), self.background_rect, 1)
        screen.blit(self.prompt_string_font_surface, (C.SCREEN_WIDTH * 0.36, C.SCREEN_HEIGHT * 0.5))


        