import pygame, json
import constants as C

class Item:
    #Item Type Code:
        #1: Weapons
        #2: Armour
        #3: Shoes
        #4: Ring
        #5: Auxillary - (5, 1) Health, (5, 2) Strength, (5, 3) Speed
    def __init__(self, name, item_type, image_path, strength=0, speed=0, armour=0, regeneration=0, durability=0, row_index=None, col_index=None):
        self.name = name
        #types: weapon = 1, armour = 2, shoes = 3, ring = 4, auxillary = 5
        self.item_type = item_type
        self.item_image = pygame.transform.scale(pygame.image.load(image_path), (C.BLOCK_WIDTH * 1.75, C.BLOCK_HEIGHT * 1.75))
        self.item_stats = {
            "strength" : strength,
            "armour" : armour,
            "speed" : speed,
            "regeneration" : regeneration,
            "durability" : durability,
        }
        self.durability = durability
        self.remaining_durability = durability
        self.applied = False

    def obtain_item(self, player_character_inventory):
        if len(player_character_inventory) < 28:
            player_character_inventory.append(self)

    def equipt_item(self, item_index, player_character):
        if player_character.inventory[item_index].item_type == 1:
            if player_character.equipped_inventory[0] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[0] = item_to_equip
        elif player_character.inventory[item_index].item_type == 2:
            if player_character.equipped_inventory[1] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[1] = item_to_equip
        elif player_character.inventory[item_index].item_type == 3:
            if player_character.equipped_inventory[2] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[2] = item_to_equip
        elif player_character.inventory[item_index].item_type == 4:
            if player_character.equipped_inventory[3] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[3] = item_to_equip
        else: #player_character.inventory[item_index].item_type == 5:
            if player_character.equipped_inventory[4] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                #item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[4] = item_to_equip
            elif player_character.equipped_inventory[5] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                #item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[5] = item_to_equip
            elif player_character.equipped_inventory[6] == None:
                item_to_equip = player_character.inventory.pop(item_index)
                #Apply item's effects
                #item_to_equip.apply_item(player_character)
                player_character.equipped_inventory[6] = item_to_equip

    def unequipt_item(self, item_index, player_character):
        if len(player_character.inventory) < 28:
            item_to_unequipt = player_character.equipped_inventory.pop(item_index)
            #Remove item's effects
            if item_to_unequipt.item_type in range (1, 5):
                item_to_unequipt.unapply_item(player_character)
            #Switch item's inventory
            player_character.equipped_inventory.insert(item_index, None)
            player_character.inventory.append(item_to_unequipt)
    
    def apply_item(self, player_character):
        player_character.strength += self.item_stats['strength']
        player_character.speed -= self.item_stats['speed'] * 1000
        player_character.armour += self.item_stats['armour']
        player_character.health_regeneration += self.item_stats['regeneration']
        self.applied = True

    def unapply_item(self, player_character):
        player_character.strength -= self.item_stats['strength']
        player_character.speed += self.item_stats['speed'] * 1000
        player_character.armour -= self.item_stats['armour']
        player_character.health_regeneration -= self.item_stats['regeneration']
        self.applied = False        

    def discard_item(self, item_index, player_character_inventory):
        player_character_inventory.pop(item_index)
        del self

class AuxItem(Item):
    def __init__(self, name, item_type, image_path, effect_magnitude, duration):
        self.name = name
        self.item_type = item_type
        self.item_image = pygame.transform.scale(pygame.image.load(image_path), (C.BLOCK_WIDTH * 1.75, C.BLOCK_HEIGHT * 1.75))
        self.effect_magnitude = effect_magnitude
        self.duration = duration
        self.applied = False

    def apply_aux_item(self, player_character, num_input):
        if self.item_type == (5, 1):
            player_character.health += self.effect_magnitude
            if player_character.health > 100:
                player_character.health = 100
            player_character.equipped_inventory[3 + num_input] = None
        elif self.item_type == (5, 2):
            player_character.player_statuses.append((self.effect_magnitude, self.duration, self.item_type, pygame.time.get_ticks()))
            player_character.strength += self.effect_magnitude
            player_character.equipped_inventory[3 + num_input] = None
        elif self.item_type == (5, 3):
            player_character.player_statuses.append((self.effect_magnitude, self.duration, self.item_type, pygame.time.get_ticks()))
            player_character.speed -= self.effect_magnitude * 1000
            player_character.equipped_inventory[3 + num_input] = None

def create_item(item_data):
    if item_data['row, col'][0] == 4:
        if "Potion" in item_data['name']:
            if "Health" in item_data['name']:
                name = item_data['name']
                item_type = (5, 1)
                image_path = "images/potion1.png"
                effect_magnitude = item_data['restoration']
                duration = 0
            elif "Strength" in item_data['name']:
                name = item_data['name']
                item_type = (5, 2)
                image_path = "images/potion2.png"
                effect_magnitude = item_data['boost']
                duration = item_data['duration']
            elif "Speed" in item_data['name']:
                name = item_data['name']
                item_type = (5, 3)
                image_path = "images/potion3.png"
                effect_magnitude = item_data['boost']
                duration = item_data['duration']
        return(AuxItem(name, item_type, image_path, effect_magnitude, duration))
    else:
        name = item_data['name']
        if item_data['row, col'][0] == 0:
            item_type = 1
            image_path = "images/sword.png"
        elif item_data['row, col'][0] == 1:
            item_type = 2
            image_path = "images/armour.png"
        elif item_data['row, col'][0] == 2:
            item_type = 3
            image_path = "images/shoe.png"
        elif item_data['row, col'][0] == 3:
            item_type = 4
            image_path = "images/ring.png"
        strength = item_data['strength']
        speed = item_data['speed']
        armour = item_data['armour']
        regeneration = item_data['regeneration']
        durability = item_data['durability']
        return(Item(name, item_type, image_path, strength, speed, armour, regeneration, durability))


class InventoryNavigator:
    def __init__(self):
        self.active = False
        self.nav_row = 1
        self.nav_col = 0
    
    #Key input code:
        #W = 1
        #S = 2
        #A = 3
        #D = 4
    def navigator_move(self, key_input):
        if key_input == 1:
            if self.nav_row - 1 >= 0:
                self.nav_row -= 1
        elif key_input == 2:
            if self.nav_row + 1 <= 4:
                self.nav_row += 1
        elif key_input == 3:
            if self.nav_col - 1 >= 0:
                self.nav_col -= 1
        elif key_input == 4:
            if self.nav_col + 1 <= 6:
                self.nav_col += 1

    def get_item_info(self, player_character):
        if self.nav_row == 0:
            index = self.nav_col
            if player_character.equipped_inventory[index] != None: 
                item_to_get = player_character.equipped_inventory[index]
            else:
                item_to_get = None
        elif self.nav_row >= 1:
            index = (self.nav_row - 1) * 7 + self.nav_col
            if (0 <= index) and (index < len(player_character.inventory)): 
                item_to_get = player_character.inventory[index]
            else:
                item_to_get = None
        if item_to_get != None:
            if item_to_get.item_type in range (1, 6):
                display_string = ["Name: {}".format(item_to_get.name), "Strength: {}".format(item_to_get.item_stats['strength']), 
                                "Speed: {}".format(item_to_get.item_stats['speed']), "Armour: {}".format(item_to_get.item_stats['armour']),
                                "Regeneration: {}".format(item_to_get.item_stats['regeneration']), "Durability: {}/{}".format(item_to_get.item_stats['durability'], item_to_get.remaining_durability)]
            elif item_to_get.item_type == (5, 1):
                display_string = ["Name: {}".format(item_to_get.name), "Restoration: {}".format(item_to_get.effect_magnitude)]
            elif item_to_get.item_type == (5, 2) or item_to_get.item_type == (5, 3):
                display_string = ["Name: {}".format(item_to_get.name), "Boost: {}".format(item_to_get.effect_magnitude), "Duration: {}".format(item_to_get.duration)]
            return(display_string)               
        else:
            return (item_to_get)           

class Shop:
    def __init__(self):
        self.shop_items = None
        with open("items.json", "r") as f:
            self.shop_items = json.load(f)

class ShopNavigator:
    def __init__(self):
        self.active = False
        self.nav_row = 0
        self.nav_col = 0

    def navigator_move(self, key_input):
        if key_input == 1:
            if self.nav_row - 1 >= 0:
                self.nav_row -= 1
        elif key_input == 2:
            if self.nav_row + 1 <= 5:
                self.nav_row += 1
        elif key_input == 3:
            if self.nav_col - 1 >= 0:
                self.nav_col -= 1
        elif key_input == 4:
            if self.nav_col + 1 <= 7:
                self.nav_col += 1

    def buy_item(self, shop_items):
        for item_type in shop_items: 
            for row_col in item_type.values():
                for item in row_col:
                    if item['row, col'][0] == self.nav_row and item['row, col'][1] == self.nav_col:
                        return(item)

    def get_item_info(self, shop_items):
        for item_type in shop_items: 
            for row_col in item_type.values():
                for stat in row_col:
                    if stat['row, col'][0] == self.nav_row and stat['row, col'][1] == self.nav_col:
                        if list(item_type.keys())[0] != "POTIONS":
                            display_string = ["Name: {}".format(stat['name']), "Cost: {}".format(stat['cost']), "Strength: {}".format(stat['strength']),
                                            "Armour: {}".format(stat['armour']), "Speed: {}".format(stat['speed']), "Regeneration: {}".format(stat['regeneration']),
                                            "Durability: {}".format(stat['durability'])]
                            return(display_string)
                        elif list(item_type.keys())[0] == "POTIONS":
                            display_string = ["{}: {}".format(key.capitalize(), value) for key, value in stat.items() if key != 'row, col']
                            return(display_string)
                        else:
                            return(None)
