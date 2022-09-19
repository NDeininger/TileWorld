import pygame, sys
import constants as C

class StartScreen:
    def __init__(self):
        self.title_font = pygame.font.Font(None, 32)
        self.controls_string = ['USER CONTROLS', 'Movement: Arrow Keys', 'Attack: Space Bar',
                                'Inventory: I', 'Menu Navigation: WSAD', 'Equip/Unequip/Buy: E',
                                'Get Item Info: Q', 'Discard Item: X', 'Open/Close Shop: B',
                                'Use Auxiliary Items: 1-3']
        self.controls_font = pygame.font.Font(None, 32)
        self.instructions_font = pygame.font.Font(None, 30)
        self.title_font_surface = self.title_font.render(C.GAME_TITLE, True, (224, 224, 224))
        self.instructions_font_surface = self.instructions_font.render("Survive as long as possible by defeating enemies and collecting coins!", True, (224, 224, 224))
        self.start_string_font_surface = self.instructions_font.render("Press Enter to begin playing!", True, (224, 224, 224))
        self.end_string_font_surface = self.instructions_font.render("Press ESC to end game session.", True, (224, 224, 224))
        self.screen_background_rect = pygame.Rect(0, 0, C.MONITOR.width, C.MONITOR.height)
        self.title_insturctions_rect = pygame.Rect(C.MONITOR.width * 0.35, C.MONITOR.height * 0.05, 700, 90)
        self.controls_rect = pygame.Rect(C.MONITOR.width * 0.15, C.MONITOR.height * 0.6, 310, 322)
    
    def display_start(self, screen):
        while 1:
            pygame.draw.rect(screen, (0,0,0), self.screen_background_rect)
            pygame.draw.rect(screen, (204,0,204), self.title_insturctions_rect)
            pygame.draw.rect(screen, (204,0,204), self.controls_rect)
            screen.blit(self.title_font_surface, (C.MONITOR.width * 0.5, C.MONITOR.height * 0.06))
            screen.blit(self.instructions_font_surface, (C.MONITOR.width * 0.35, C.MONITOR.height * 0.06 + 32))
            control_string_index = 0
            for string in self.controls_string:
                self.controls_string_font_surface = self.controls_font.render(string, True, (224, 224, 224))
                screen.blit(self.controls_string_font_surface, (C.MONITOR.width * 0.152, (C.MONITOR.height * 0.61) + (control_string_index * 32)))
                control_string_index += 1
            screen.blit(self.start_string_font_surface, (C.MONITOR.width *  0.7, C.MONITOR.height * 0.8))
            screen.blit(self.end_string_font_surface, (C.MONITOR.width *  0.7, C.MONITOR.height * 0.8 + 30))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return None
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
class PlayerDeathScreen:
    def __init__(self):
        self.message_font = pygame.font.Font(None, 72)
        self.message_font2 = pygame.font.Font(None, 56)
        self.message_font_surface1 = self.message_font.render("You Died...", True, (204, 0, 0))
        self.message_font_surface2 = self.message_font.render("Game Over!", True, (204, 0, 0))
        self.message_font_surface3 = self.message_font2.render("Press ESC To End Session", True, (204, 0, 0))
        self.background_rect = pygame.Rect(0, 0, C.MONITOR.width, C.MONITOR.height)
    
    def display_death(self, screen):
        while 1:
            pygame.draw.rect(screen, (0, 0, 0), self.background_rect)
            screen.blit(self.message_font_surface1, (C.MONITOR.width * 0.45, C.MONITOR.height * 0.10))
            screen.blit(self.message_font_surface2, (C.MONITOR.width * 0.45, C.MONITOR.height * 0.10 + 72))
            screen.blit(self.message_font_surface3, (C.MONITOR.width * 0.06, C.MONITOR.height * 0.90))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
