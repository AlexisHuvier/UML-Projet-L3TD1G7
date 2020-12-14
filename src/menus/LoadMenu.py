import pygame

class LoadMenu:
    def __init__(self, game):
        self.game = game
        
        self.background = pygame.Surface((800, 500), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 22).render("Charger Sauvegarde", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 22).size("Charger Sauvegarde")

        self.coming_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.coming_button.fill((50, 50, 50))
        coming_title = pygame.font.SysFont("Arial", 16).render("Coming Soon", True, (255, 255, 255))
        coming_size = pygame.font.SysFont("Arial", 16).size("Coming Soon")
        self.coming_button.blit(coming_title, (100 - coming_size[0]/2, 20 - coming_size[1]/2))

        self.return_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.return_button.fill((50, 50, 50))
        return_title = pygame.font.SysFont("Arial", 16).render("Retour", True, (255, 255, 255))
        return_size = pygame.font.SysFont("Arial", 16).size("Retour")
        self.return_button.blit(return_title, (100 - return_size[0]/2, 20 - return_size[1]/2))

    def display(self, screen):
        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (450-self.title_size[0]/2, 100-self.title_size[1]/2))
        screen.blit(self.coming_button, (350, 275))
        screen.blit(self.return_button, (350, 425))
    
    def process_event(self, evt):
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.return_button.get_rect(x=350, y=425).collidepoint(*evt.pos):
                self.game.display(0)