#Initialize pygame
pygame.init()
screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT), pygame.FULLSCREEN)
screen.fill(C.BACKGROUND_COLOR)
pygame.display.set_caption(C.GAME_TITLE)
game_icon = pygame.image.load(C.GAME_ICON)
pygame.display.set_icon(game_icon)

#Initiate Start Screen
start_screen = screens.StartScreen()
start_screen.display_start(screen)

#Initialize game map
game_map = map.GameMap()
temp_grid = game_map.get_temp_grid(C.PLAYER_START_X_COORD, C.PLAYER_START_Y_COORD)
game_map.map_draw(screen, temp_grid)

#Initialize player character
player_character = player.Player(C.PLAYER_START_X_COORD, C.PLAYER_START_Y_COORD, C.PLAYER_START_X_POS, C.PLAYER_START_Y_POS, C.PLAYER_IMAGE_TITLE, 0)
player_character.player_draw(screen)

#Create Level Class
level = enemy.Levels()

#Create Particle Effect Objects
player_attack_particle = animations.Particle(screen)
enemy_attack_particle = animations.Particle(screen)
enemy_death_particle = animations.Particle(screen)

#Create Display Objects
statusbar_display = display.PlayerStatusBar(player_character)
inventory_display = display.PlayerInventoryDisplay()
inventory_navigator_display = display.InventoryNavigatorDisplay()
level_countdown_display = display.LevelDisplay(level)
shop_menu_display = display.ShopDisplay()
shop_menu_navigator_display = display.ShopNavigatorDisplay()
quit_prompt_display = display.QuitPrompt()


#Create death screen Object
death_screen = screens.PlayerDeathScreen()

#Create Inventory Navigator Object
inventory_navigator = inventory.InventoryNavigator()

#Initialize Shop and Shop Menu
shop = inventory.Shop()
shop_menu_navigator = inventory.ShopNavigator()

#Initialize enemy list
active_enemies = []

#Create a pygame clock object to track time
timer = pygame.time.Clock()

#Called to redraw all map entities
def redraw():
    game_map.map_draw(screen, temp_grid)
    player_character.player_draw(screen)
    for active_enemy in level.active_enemies:
        active_enemy.enemy_draw(screen)
 
#Main game loop
while 1:
    #Used to update time and to limit fps
    timer.tick(40)
    
    #Handle user input
    for event in pygame.event.get():
        #Process keydown input
        if event.type == pygame.KEYDOWN:
            #Arrow Keys - Move Player If Possible and update temp_grid for map and enemy use
            #Prevent player from moving or attacking if in inventory navigator
            if inventory_navigator.active == False and shop_menu_navigator.active == False:
                if event.key == pygame.K_LEFT:
                    player_character.theta = 90
                    if player_character.player_movement_check(game_map.map_grid[player_character.row - 1][player_character.col - 2]) == 1:
                        player_character.player_move(1)
                        temp_grid = game_map.get_temp_grid(player_character.col, player_character.row)
                if event.key == pygame.K_RIGHT:
                    player_character.theta = 270
                    if player_character.player_movement_check(game_map.map_grid[player_character.row - 1][player_character.col]) == 1:
                        player_character.player_move(2)
                        temp_grid = game_map.get_temp_grid(player_character.col, player_character.row)
                if event.key == pygame.K_UP:
                    player_character.theta = 0
                    if player_character.player_movement_check(game_map.map_grid[player_character.row - 2][player_character.col - 1]) == 1:
                        player_character.player_move(3)
                        temp_grid = game_map.get_temp_grid(player_character.col, player_character.row)
                if event.key == pygame.K_DOWN:
                    player_character.theta = 180
                    if player_character.player_movement_check(game_map.map_grid[player_character.row][player_character.col - 1]) == 1:
                        player_character.player_move(4)
                        temp_grid = game_map.get_temp_grid(player_character.col, player_character.row)
                #Space Button - Player Attack
                if event.key == pygame.K_SPACE:
                    player_character.player_attack(level.active_enemies, player_attack_particle, screen, game_map, temp_grid)
                #Number Keys 1-3 - Use Aux Item
                if event.key == pygame.K_1:
                    item_to_use = player_character.equipped_inventory[4]
                    if item_to_use != None:
                        item_to_use.apply_aux_item(player_character, 1)
                if event.key == pygame.K_2:
                    item_to_use = player_character.equipped_inventory[5]
                    if item_to_use != None:
                        item_to_use.apply_aux_item(player_character, 2)
                if event.key == pygame.K_3:
                    item_to_use = player_character.equipped_inventory[6]
                    if item_to_use != None:
                        item_to_use.apply_aux_item(player_character, 3)
            #"B" Key - Open up Shop Menu if inventory is not active
            if event.key == pygame.K_b and inventory_navigator.active == False:
                shop_menu_navigator.active = not(shop_menu_navigator.active)
                #If Shop Menu is closed and display item info or buy item prompt is still on, turn off display item info and buy item prompt too
                if shop_menu_navigator_display.item_info_active == True and shop_menu_navigator.active == False:
                    shop_menu_navigator_display.item_info_active = False
                if shop_menu_navigator_display.buy_item_prompt_active == True and shop_menu_navigator.active == False:
                    shop_menu_navigator_display.buy_item_prompt_active = False
            #WSAD + E & Q Keys - Process Shop Actions if Active
            if shop_menu_navigator.active:
                if event.key == pygame.K_w and not(shop_menu_navigator_display.item_info_active) and not(shop_menu_navigator_display.buy_item_prompt_active):
                    shop_menu_navigator.navigator_move(1)
                if event.key == pygame.K_s and not(shop_menu_navigator_display.item_info_active) and not(shop_menu_navigator_display.buy_item_prompt_active):
                    shop_menu_navigator.navigator_move(2)
                if event.key == pygame.K_a and not(shop_menu_navigator_display.item_info_active) and not(shop_menu_navigator_display.buy_item_prompt_active):
                    shop_menu_navigator.navigator_move(3)
                if event.key == pygame.K_d and not(shop_menu_navigator_display.item_info_active) and not(shop_menu_navigator_display.buy_item_prompt_active):
                    shop_menu_navigator.navigator_move(4)
                if event.key == pygame.K_e and not(shop_menu_navigator_display.item_info_active) and not(shop_menu_navigator_display.buy_item_prompt_active):
                    item_to_buy = shop_menu_navigator.buy_item(shop.shop_items)
                    if item_to_buy != None:
                        shop_menu_navigator_display.buy_item_prompt_active = not(shop_menu_navigator_display.buy_item_prompt_active)
                if shop_menu_navigator_display.buy_item_prompt_active:
                    if event.key == pygame.K_y:
                        #Conduct transaction
                        if player_character.coins >= item_to_buy['cost']:
                            bought_item = inventory.create_item(item_to_buy)
                            bought_item.obtain_item(player_character.inventory)
                            shop_menu_navigator_display.buy_item_prompt_active = not(shop_menu_navigator_display.buy_item_prompt_active)
                            player_character.coins -= item_to_buy['cost']
                            item_to_buy = None
                        else:
                            shop_menu_navigator_display.buy_item_prompt_active = not(shop_menu_navigator_display.buy_item_prompt_active)
                            shop_menu_navigator_display.insufficient_coins_prompt_active = not(shop_menu_navigator_display.insufficient_coins_prompt_active)
                    elif event.key == pygame.K_n:
                        shop_menu_navigator_display.buy_item_prompt_active = not(shop_menu_navigator_display.buy_item_prompt_active)
                        item_to_buy = None
                if event.key == pygame.K_q and not(shop_menu_navigator_display.buy_item_prompt_active):
                    display_string = shop_menu_navigator.get_item_info(shop.shop_items)
                    if display_string != None:
                        shop_menu_navigator_display.item_info_active = not(shop_menu_navigator_display.item_info_active)
            if shop_menu_navigator_display.insufficient_coins_prompt_active:
                    if event.key == pygame.K_RETURN:
                        shop_menu_navigator_display.insufficient_coins_prompt_active = not(shop_menu_navigator_display.insufficient_coins_prompt_active)
            #"I" Key - Engage/Disengage Inventory Navigator Mode
            if event.key == pygame.K_i and shop_menu_navigator.active == False:
                inventory_navigator.active = not(inventory_navigator.active)
                #If Inventory Navigator is closed and display item info or del item prompt is still on, turn off display item info and del item prompt too
                if inventory_navigator_display.item_info_active == True and inventory_navigator.active == False:
                    inventory_navigator_display.item_info_active = False
                if inventory_navigator_display.del_item_active == True and inventory_navigator.active == False:
                    inventory_navigator_display.del_item_active = False
            #WSAD + E & Q Keys - Process Inventory Navigator Actions If Active
            if inventory_navigator.active:
                if event.key == pygame.K_w and not(inventory_navigator_display.item_info_active) and not(inventory_navigator_display.del_item_active):
                    inventory_navigator.navigator_move(1)
                if event.key == pygame.K_s and not(inventory_navigator_display.item_info_active) and not(inventory_navigator_display.del_item_active):
                    inventory_navigator.navigator_move(2)
                if event.key == pygame.K_a and not(inventory_navigator_display.item_info_active) and not(inventory_navigator_display.del_item_active):
                    inventory_navigator.navigator_move(3)
                if event.key == pygame.K_d and not(inventory_navigator_display.item_info_active) and not(inventory_navigator_display.del_item_active):
                    inventory_navigator.navigator_move(4)
                if event.key == pygame.K_e and not(inventory_navigator_display.item_info_active) and not(inventory_navigator_display.del_item_active):
                    if inventory_navigator.nav_row == 0:
                        if player_character.equipped_inventory[inventory_navigator.nav_col] != None:
                            player_character.equipped_inventory[inventory_navigator.nav_col].unequipt_item(inventory_navigator.nav_col, player_character)
                    elif inventory_navigator.nav_row >= 1:
                        if 0 <= (inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col and (inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col < len(player_character.inventory):
                            player_character.inventory[(inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col].equipt_item((inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col, player_character)
                #"Q" Key - Engage/Disengage Item Info Display For Selected Item
                if event.key == pygame.K_q and not(inventory_navigator_display.del_item_active):
                    display_string = inventory_navigator.get_item_info(player_character)
                    if display_string != None:
                        inventory_navigator_display.item_info_active = not(inventory_navigator_display.item_info_active)
                #'X' Key - Activate delete item prompt
                if event.key == pygame.K_x and not(inventory_navigator_display.item_info_active):
                    if inventory_navigator.nav_row == 0:
                        if player_character.equipped_inventory[inventory_navigator.nav_col] != None:
                            inventory_navigator_display.del_item_active = not(inventory_navigator_display.del_item_active)
                    elif inventory_navigator.nav_row >= 1:
                        if 0 <= (inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col and (inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col < len(player_character.inventory):
                            inventory_navigator_display.del_item_active = not(inventory_navigator_display.del_item_active)    
                #If delete item prompt is active, check to see if player enters y or n, delete item if y, remove prompt if n
                if inventory_navigator_display.del_item_active:
                    if event.key == pygame.K_y:
                        if inventory_navigator.nav_row == 0:
                            player_character.equipped_inventory[inventory_navigator.nav_col].unapply_item(player_character)
                            player_character.equipped_inventory[inventory_navigator.nav_col].discard_item(inventory_navigator.nav_col, player_character.equipped_inventory)
                            player_character.equipped_inventory.insert(inventory_navigator.nav_col, None)
                        elif inventory_navigator.nav_row >= 1:
                            player_character.inventory[(inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col].discard_item((inventory_navigator.nav_row - 1) * 7 + inventory_navigator.nav_col, player_character.inventory)
                        inventory_navigator_display.del_item_active = not(inventory_navigator_display.del_item_active)
                    elif event.key == pygame.K_n:
                        inventory_navigator_display.del_item_active = not(inventory_navigator_display.del_item_active)
            #Quit game if escape is pushed, get player confirmation
            if event.key == pygame.K_ESCAPE:
                quit_prompt = True
                if quit_prompt:
                    quit_prompt_display.quit_prompt_display(screen)
                    pygame.display.update()
                while quit_prompt:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_y:
                                pygame.quit()
                                sys.exit()
                            elif event.key == pygame.K_n:
                                quit_prompt = False
        #Quit if program manually stopped
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Check to see if spawning more enemies is possible, chance to spawn enemy in random spot if true. Increase difficulty as game progresses.
    level.enemy_spawn(game_map)
    level.level_timer_check_update()
    
    #Process active enemy actions
    for active_enemy in level.active_enemies:
        #Check to see if enemy is alive. If not, remove and initiate death animation
        if active_enemy.health <= 0:
            player_character.coins += random.randint(0, 3)
            level.active_enemies.remove(active_enemy)
            #Enemy death animation
            duration = 20 
            while duration > 0:
                redraw()
                enemy_death_particle.create_particles(active_enemy.col_pos + (0.5 * C.BLOCK_WIDTH), active_enemy.row_pos + (0.5 * C.BLOCK_HEIGHT), 9, random.randint(-3, 3), random.randint(-5, -1), 1, (160, 160, 160))
                enemy_death_particle.animate_particles()
                pygame.display.update()
                duration -= 1
            enemy_death_particle.particles = []
            del active_enemy
            continue
        #Check to see if player in range, aggravated if so
        active_enemy.enemy_detect(player_character.row, player_character.col)
        #Random Movement for non-aggravated enemies
        if active_enemy.aggravated == False:
            move_roll = random.randrange(1,401)
            if move_roll == 1:
                active_enemy.theta = 90
                if active_enemy.enemy_movement_check(game_map.map_grid[active_enemy.row - 1][active_enemy.col - 2]) == 1:
                    active_enemy.enemy_move(1)
            elif move_roll == 2:
                active_enemy.theta = 270
                if active_enemy.enemy_movement_check(game_map.map_grid[active_enemy.row - 1][active_enemy.col]) == 1:
                    active_enemy.enemy_move(2)
            elif move_roll == 3:
                active_enemy.theta = 0
                if active_enemy.enemy_movement_check(game_map.map_grid[active_enemy.row - 2][active_enemy.col - 1]) == 1:
                    active_enemy.enemy_move(3)
            elif move_roll == 4:
                active_enemy.theta = 180
                if active_enemy.enemy_movement_check(game_map.map_grid[active_enemy.row][active_enemy.col - 1]) == 1:
                    active_enemy.enemy_move(4)
        #Movement for aggravated enemies
        elif active_enemy.aggravated == True:
            move_roll = random.randrange(1,160)
            if move_roll in range(1, 5):
                active_enemy.enemy_move(move_roll, player_character.row, player_character.col, game_map.map_grid)
            #Check to see if enemy in range for attack. If so, attempt attack
            if abs(player_character.row - active_enemy.row) + abs(player_character.col - active_enemy.col) <= 1:
                active_enemy.enemy_attack(level.active_enemies, player_character, enemy_attack_particle, screen, game_map, temp_grid, shop_menu_navigator.active)
        #Check for enemies to display, set actual pos if needed
        active_enemy.enemy_display_check(temp_grid)
    
    #Check for Player Death
    if player_character.health <= 0:
        death_screen.display_death(screen)

    #Apply Player statuses
    player_character.check_player_statuses()

    #Redraw map and entities with updated changes
    redraw()

    #Apply Player Health Regeneration
    if player_character.health < 100 and player_character.health_regeneration <= (100 - player_character.health):
        player_character.health += player_character.health_regeneration
    elif player_character.health < 100 and player_character.health_regeneration > (100 - player_character.health):
        player_character.health += (100 - player_character.health)
    player_character.health_regeneration =  round(player_character.health_regeneration, 2)

    #Update Player Status Bar
    statusbar_display.statusbar_display(screen, player_character)
    
    #Update Player Inventory Display
    inventory_display.inventory_setup_display(screen)
    
    #Update Player Inventory Item Slot Displays
    inventory_display.player_inventory_display(screen, player_character.inventory)
    inventory_display.player_equipped_display(screen, player_character.equipped_inventory)
    if inventory_navigator.active:
        inventory_navigator_display.display_nav_rect(screen, inventory_navigator.nav_row, inventory_navigator.nav_col)
    if inventory_navigator_display.item_info_active:
        inventory_navigator_display.display_item_info(screen, display_string, inventory_navigator.nav_row, inventory_navigator.nav_col)
    if inventory_navigator_display.del_item_active:
        inventory_navigator_display.del_item_prompt(screen, inventory_navigator.nav_row, inventory_navigator.nav_col)

    #Update Level and Countdown Display
    level_countdown_display.level_display_update(level)
    level_countdown_display.level_countdown_display(screen)

    #Update Shop Menu If Active
    if shop_menu_navigator.active:
        shop_menu_display.display_shop(screen)
        shop_menu_display.display_shop_items(screen)
        shop_menu_navigator_display.display_nav_rect(screen, shop_menu_navigator.nav_row, shop_menu_navigator.nav_col)
    if shop_menu_navigator_display.item_info_active:
        shop_menu_navigator_display.display_item_info(screen, display_string, shop_menu_navigator.nav_row, shop_menu_navigator.nav_col)
    if shop_menu_navigator_display.buy_item_prompt_active:
        (shop_menu_navigator_display.buy_item_prompt(screen, shop_menu_navigator.nav_row, shop_menu_navigator.nav_col))
    if shop_menu_navigator_display.insufficient_coins_prompt_active:
        shop_menu_navigator_display.insufficient_coins_prompt(screen)

    #Update screen display
    pygame.display.update()