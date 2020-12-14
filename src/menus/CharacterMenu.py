import pygame

class CharacterMenu:
    def __init__(self, game):
        self.game = game
        
        self.background = pygame.Surface((800, 500), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 22).render("Choix du personnage", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 22).size("Choix du personnage")

        self.standart_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.standart_button.fill((50, 50, 50))
        standart_title = pygame.font.SysFont("Arial", 16).render("Standart", True, (255, 255, 255))
        standart_size = pygame.font.SysFont("Arial", 16).size("Standart")
        self.standart_button.blit(standart_title, (100 - standart_size[0]/2, 20 - standart_size[1]/2))

        self.hippie_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.hippie_button.fill((50, 50, 50))
        hippie_title = pygame.font.SysFont("Arial", 16).render("Hippie", True, (255, 255, 255))
        hippie_size = pygame.font.SysFont("Arial", 16).size("Hippie")
        self.hippie_button.blit(hippie_title, (100 - hippie_size[0]/2, 20 - hippie_size[1]/2))

        self.presse_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.presse_button.fill((50, 50, 50))
        presse_title = pygame.font.SysFont("Arial", 16).render("Homme Pressé", True, (255, 255, 255))
        presse_size = pygame.font.SysFont("Arial", 16).size("Homme Pressé")
        self.presse_button.blit(presse_title, (100 - presse_size[0]/2, 20 - presse_size[1]/2))

    def display(self, screen):
        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (450-self.title_size[0]/2, 100-self.title_size[1]/2))
        screen.blit(self.standart_button, (350, 225))
        screen.blit(self.hippie_button, (350, 325))
        screen.blit(self.presse_button, (350, 425))
    
    def process_event(self, evt):
        pass