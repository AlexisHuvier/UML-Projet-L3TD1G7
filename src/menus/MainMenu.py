import pygame

class MainMenu:
    def __init__(self, game):
        self.game = game
        
        self.background = pygame.Surface((1100, 800), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 30).render("UMLProject", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 30).size("UMLProject")

        self.play_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.play_button.fill((50, 50, 50))
        play_title = pygame.font.SysFont("Arial", 16).render("Jouer", True, (255, 255, 255))
        play_size = pygame.font.SysFont("Arial", 16).size("Jouer")
        self.play_button.blit(play_title, (100 - play_size[0]/2, 20 - play_size[1]/2))

        self.load_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.load_button.fill((50, 50, 50))
        load_title = pygame.font.SysFont("Arial", 16).render("Charger Sauvegarde", True, (255, 255, 255))
        load_size = pygame.font.SysFont("Arial", 16).size("Charger Sauvegarde")
        self.load_button.blit(load_title, (100 - load_size[0]/2, 20 - load_size[1]/2))

        self.quit_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.quit_button.fill((50, 50, 50))
        quit_title = pygame.font.SysFont("Arial", 16).render("Quitter", True, (255, 255, 255))
        quit_size = pygame.font.SysFont("Arial", 16).size("Quitter")
        self.quit_button.blit(quit_title, (100 - quit_size[0]/2, 20 - quit_size[1]/2))

    def display(self, screen):
        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (600-self.title_size[0]/2, 150-self.title_size[1]/2))
        screen.blit(self.play_button, (500, 325))
        screen.blit(self.load_button, (500, 525))
        screen.blit(self.quit_button, (500, 725))
    
    def process_event(self, evt):
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.quit_button.get_rect(x=500, y=725).collidepoint(*evt.pos):
                self.game.stop()
            elif self.play_button.get_rect(x=500, y=325).collidepoint(*evt.pos):
                self.game.display(1)
            elif self.load_button.get_rect(x=500, y=525).collidepoint(*evt.pos):
                self.game.display(2)