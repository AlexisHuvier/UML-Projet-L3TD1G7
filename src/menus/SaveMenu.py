import pygame
import string

class SaveMenu:
    def __init__(self, game):
        self.game = game
        self.text = ""
        self.focus = False
        
        self.background = pygame.Surface((800, 500), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 22).render("Sauvegarder", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 22).size("Sauvegarder")

        self.save_entry = pygame.Surface((400, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_entry.fill((50, 50, 50))
        white = pygame.Surface((392, 32))
        white.fill((255, 255, 255))
        self.save_entry.blit(white, (4, 4))
        self.save_text = pygame.font.SysFont("Arial", 16).render(self.text, True, (0, 0, 0))
        self.save_tsize = pygame.font.SysFont("Arial", 16).size(self.text)

        self.save_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_button.fill((50, 50, 50))
        save_title = pygame.font.SysFont("Arial", 16).render("Sauvegarder", True, (255, 255, 255))
        save_size = pygame.font.SysFont("Arial", 16).size("Sauvegarder")
        self.save_button.blit(save_title, (100 - save_size[0]/2, 20 - save_size[1]/2))

        self.return_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.return_button.fill((50, 50, 50))
        return_title = pygame.font.SysFont("Arial", 16).render("Retour", True, (255, 255, 255))
        return_size = pygame.font.SysFont("Arial", 16).size("Retour")
        self.return_button.blit(return_title, (100 - return_size[0]/2, 20 - return_size[1]/2))

    def update_text(self):
        self.save_text = pygame.font.SysFont("Arial", 16).render(self.text, True, (0, 0, 0))
        self.save_tsize = pygame.font.SysFont("Arial", 16).size(self.text)

    def display(self, screen):
        x = 400 - self.save_tsize[0] - 10
        if x > 10:
            x = 10
        y = 20 - self.save_tsize[1] / 2

        screen.blit(self.background, (50, 50))
        screen.blit(self.title, (450-self.title_size[0]/2, 100-self.title_size[1]/2))
        screen.blit(self.save_entry, (250, 255))
        screen.blit(self.save_text, (250+x, 255+y))
        screen.blit(self.save_button, (200, 400))
        screen.blit(self.return_button, (500, 400))
    
    def process_event(self, evt):
        if evt.type == pygame.KEYDOWN and self.focus:
            if evt.key == pygame.K_BACKSPACE:
                if len(self.text):
                    self.text = self.text[:-1]
                    self.update_text()
        elif evt.type == pygame.TEXTINPUT and self.focus:
            if evt.text in string.ascii_letters+string.digits+" ":
                if self.save_tsize[0] < 365:
                    self.text += evt.text
                    self.update_text()
        elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.save_entry.get_rect(x=250, y=255).collidepoint(*evt.pos):
                self.focus = True
            else:
                if self.save_button.get_rect(x=200, y=400).collidepoint(*evt.pos):
                    print("SAVE")
                elif self.return_button.get_rect(x=500, y=400).collidepoint(*evt.pos):
                    self.game.display(4)
                self.focus = False
            