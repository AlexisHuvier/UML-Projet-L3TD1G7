import pygame
import string

from src.utils import Save

class SaveMenu:
    def __init__(self, game):
        self.game = game
        self.text = ""
        self.focus = False
        
        # Création du fond
        self.background = pygame.Surface((1100, 800), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 30).render("Sauvegarder", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 30).size("Sauvegarder")

        # Création de l'entrée de texte
        self.save_entry = pygame.Surface((400, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_entry.fill((50, 50, 50))
        white = pygame.Surface((392, 32))
        white.fill((255, 255, 255))
        self.save_entry.blit(white, (4, 4))
        self.save_text = pygame.font.SysFont("Arial", 16).render(self.text, True, (0, 0, 0))
        self.save_tsize = pygame.font.SysFont("Arial", 16).size(self.text)

        # Création du bouton Sauvegarder
        self.save_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_button.fill((50, 50, 50))
        save_title = pygame.font.SysFont("Arial", 16).render("Sauvegarder", True, (255, 255, 255))
        save_size = pygame.font.SysFont("Arial", 16).size("Sauvegarder")
        self.save_button.blit(save_title, (100 - save_size[0]/2, 20 - save_size[1]/2))

        # Création du bouton retour
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
        screen.blit(self.title, (600-self.title_size[0]/2, 150-self.title_size[1]/2))
        screen.blit(self.save_entry, (400, 450))
        screen.blit(self.save_text, (400+x, 450+y))
        screen.blit(self.save_button, (300, 725))
        screen.blit(self.return_button, (750, 725))
    
    def process_event(self, evt):
        if evt.type == pygame.KEYDOWN and self.focus:
            if evt.key == pygame.K_BACKSPACE: # Effacer du texte
                if len(self.text):
                    self.text = self.text[:-1]
                    self.update_text()
        elif evt.type == pygame.TEXTINPUT and self.focus: # Ajouter du texte
            if evt.text in string.ascii_letters+string.digits+" ":
                if self.save_tsize[0] < 365:
                    self.text += evt.text
                    self.update_text()
        elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
            if self.save_entry.get_rect(x=400, y=450).collidepoint(*evt.pos): # Appui sur l'entrée de texte
                self.focus = True
            else:
                if self.save_button.get_rect(x=300, y=725).collidepoint(*evt.pos): # Appui sur le bouton Sauvegarder
                    # Sauvegarde
                    save = Save(self.text)
                    save.set("player.type", self.game.player.__class__.__name__)
                    save.set("player.life", self.game.player.life)
                    save.set("player.hydration", self.game.player.hydration)
                    save.set("player.satiety", self.game.player.satiety)
                    save.set("player.mentality", self.game.player.mentality)
                    save.set("player.position", list(self.game.player.position))
                    save.set("player.go_position", list(self.game.player.go_position))
                    save.set("player.movement_mode", self.game.player.movement_mode)
                    save.set("player.has_swimsuit", self.game.player.has_swimsuit)
                    save.set("player.arrest_count", self.game.player.arrest_count)
                    save.set("player.diploma_counter", self.game.player.diplomaCounter)
                    save.set("player.diploma_obtaining_bonus", self.game.player.diplomaObtainingBonus)
                    save.set("map", [[cell.__class__.__name__ for cell in i]for i in self.game.map.case])
                    save.save()
                elif self.return_button.get_rect(x=750, y=725).collidepoint(*evt.pos): # Appui sur le bouton Retour
                    self.game.display(4)
                self.focus = False
            