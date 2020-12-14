import pygame

class PauseMenu:
    def __init__(self, game):
        self.game = game
        
        self.background = pygame.Surface((800, 500), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 22).render("Pause", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 22).size("Pause")

        self.resume_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.resume_button.fill((50, 50, 50))
        resume_title = pygame.font.SysFont("Arial", 16).render("Reprendre", True, (255, 255, 255))
        resume_size = pygame.font.SysFont("Arial", 16).size("Reprendre")
        self.resume_button.blit(resume_title, (100 - resume_size[0]/2, 20 - resume_size[1]/2))

        self.save_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_button.fill((50, 50, 50))
        save_title = pygame.font.SysFont("Arial", 16).render("Sauvegarder", True, (255, 255, 255))
        save_size = pygame.font.SysFont("Arial", 16).size("Sauvegarder")
        self.save_button.blit(save_title, (100 - save_size[0]/2, 20 - save_size[1]/2))

        self.quit_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.quit_button.fill((50, 50, 50))
        quit_title = pygame.font.SysFont("Arial", 16).render("Quitter", True, (255, 255, 255))
        quit_size = pygame.font.SysFont("Arial", 16).size("Quitter")
        self.quit_button.blit(quit_title, (100 - quit_size[0]/2, 20 - quit_size[1]/2))

    def display(self, screen):
        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (450-self.title_size[0]/2, 100-self.title_size[1]/2))
        screen.blit(self.resume_button, (350, 225))
        screen.blit(self.save_button, (350, 325))
        screen.blit(self.quit_button, (350, 425))
    
    def process_event(self, evt):
        if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.quit_button.get_rect(x=350, y=425).collidepoint(*evt.pos):
                self.game.display(0)
            elif self.resume_button.get_rect(x=350, y=225).collidepoint(*evt.pos):
                print("RESUME")
            elif self.save_button.get_rect(x=350, y=325).collidepoint(*evt.pos):
                self.game.display(3)