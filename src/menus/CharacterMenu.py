import pygame

class CharacterMenu:
    def __init__(self, game):
        self.game = game
        
        # Creation du fond
        self.background = pygame.Surface((1100, 800), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 30).render("Choix du personnage", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 30).size("Choix du personnage")

        # Creation du bouton Standard
        self.standart_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.standart_button.fill((50, 50, 50))
        standart_title = pygame.font.SysFont("Arial", 16).render("Standard", True, (255, 255, 255))
        standart_size = pygame.font.SysFont("Arial", 16).size("Standard")
        self.standart_button.blit(standart_title, (100 - standart_size[0]/2, 20 - standart_size[1]/2))

        # Creation du bouton Hippie
        self.hippie_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.hippie_button.fill((50, 50, 50))
        hippie_title = pygame.font.SysFont("Arial", 16).render("Hippie", True, (255, 255, 255))
        hippie_size = pygame.font.SysFont("Arial", 16).size("Hippie")
        self.hippie_button.blit(hippie_title, (100 - hippie_size[0]/2, 20 - hippie_size[1]/2))

        # Creation du bouton Homme pressé
        self.presse_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.presse_button.fill((50, 50, 50))
        presse_title = pygame.font.SysFont("Arial", 16).render("Homme Pressé", True, (255, 255, 255))
        presse_size = pygame.font.SysFont("Arial", 16).size("Homme Pressé")
        self.presse_button.blit(presse_title, (100 - presse_size[0]/2, 20 - presse_size[1]/2))

    def display(self, screen):
        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (600-self.title_size[0]/2, 150-self.title_size[1]/2))
        screen.blit(self.standart_button, (500, 325))
        screen.blit(self.hippie_button, (500, 525))
        screen.blit(self.presse_button, (500, 725))
    
    def process_event(self, evt):
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.standart_button.get_rect(x=500, y=325).collidepoint(*evt.pos): # Appui du bouton Standard
                self.game.create_player(0)
                self.game.display(5)
            elif self.hippie_button.get_rect(x=500, y=525).collidepoint(*evt.pos): # Appui du bouton Hippie
                self.game.create_player(1)
                self.game.display(5)
            elif self.presse_button.get_rect(x=500, y=725).collidepoint(*evt.pos): # Appui du bouton Homme pressé
                self.game.create_player(2)
                self.game.display(5)