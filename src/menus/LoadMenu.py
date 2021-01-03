import pygame
import string

from src.utils import Save
from src.Character import Hippy, HurriedMan, Standard

from src.tiles import *
from src.tiles.buildings import *

class LoadMenu:
    def __init__(self, game):
        self.game = game
        self.text = ""
        self.focus = False
        
        self.background = pygame.Surface((1100, 800), pygame.SRCALPHA, 32).convert_alpha()
        self.background.fill((100, 100, 100))
        self.title = pygame.font.SysFont("Arial", 30).render("Charger Sauvegarde", True, (255, 255, 255))
        self.title_size = pygame.font.SysFont("Arial", 30).size("Charger Sauvegarde")

        self.save_entry = pygame.Surface((400, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.save_entry.fill((50, 50, 50))
        white = pygame.Surface((392, 32))
        white.fill((255, 255, 255))
        self.save_entry.blit(white, (4, 4))
        self.save_text = pygame.font.SysFont("Arial", 16).render(self.text, True, (0, 0, 0))
        self.save_tsize = pygame.font.SysFont("Arial", 16).size(self.text)

        self.load_button = pygame.Surface((200, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.load_button.fill((50, 50, 50))
        save_title = pygame.font.SysFont("Arial", 16).render("Charger", True, (255, 255, 255))
        save_size = pygame.font.SysFont("Arial", 16).size("Charger")
        self.load_button.blit(save_title, (100 - save_size[0]/2, 20 - save_size[1]/2))

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
        screen.blit(self.load_button, (300, 725))
        screen.blit(self.return_button, (750, 725))
    
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
            if self.save_entry.get_rect(x=400, y=450).collidepoint(*evt.pos):
                self.focus = True
            else:
                if self.load_button.get_rect(x=300, y=725).collidepoint(*evt.pos):
                    save = Save(self.text)
                    save.load()
                    self.game.map.case = []
                    map_cases = save.get("map", [])
                    house_pos = (0, 0)
                    if len(map_cases) == 0:
                        self.game.map.generateMap(self.game.n, self.game.m)
                    else:
                        for x, line in enumerate(map_cases):
                            self.game.map.case.append([])
                            for y, cell in enumerate(line):
                                if cell == "House":
                                    house_pos = [x*64, y*64]
                                self.game.map.case[x].append(eval(cell+"((x*64, y*64))"))
                    type_ = save.get("player.type", "Standard")
                    if type_ == "Standard":
                        self.game.player = Standard(self.game, (0, 0), (0, 0), 0, False, 0)
                        self.game.player.life = save.get("player.life", 75)
                        self.game.player.hydration = save.get("player.hydration", 75)
                        self.game.player.satiety = save.get("player.satiery", 75)
                        self.game.player.mentality = save.get("player.mentality", 75)
                    elif type_ == "Hippy":
                        self.game.player = Hippy(self.game, (0, 0), (0, 0), 0, False, 0)
                        self.game.player.life = save.get("player.life", 75)
                        self.game.player.hydration = save.get("player.hydration", 50)
                        self.game.player.satiety = save.get("player.satiery", 50)
                        self.game.player.mentality = save.get("player.mentality", 100)
                    else:
                        self.game.player = HurriedMan(self.game, (0, 0), (0, 0), 0, False, 0)
                        self.game.player.life = save.get("player.life", 100)
                        self.game.player.hydration = save.get("player.hydration", 75)
                        self.game.player.satiety = save.get("player.satiery", 75)
                        self.game.player.mentality = save.get("player.mentality", 50)
                    self.game.player.position = save.get("player.position", house_pos)
                    self.game.player.go_position = save.get("player.go_position", (0, 0))
                    self.game.player.movement_mode = save.get("player.movement_mode", 0)
                    self.game.player.has_swimsuit = bool(save.get("player.has_swimsuit", False))
                    self.game.player.arrest_count = save.get("player.arrest_count", 0)
                    self.game.player.diplomaCounter = save.get("player.diploma_counter", 0)
                    self.game.player.diplomaObtainingBonus = save.get("player.diploma_obtaining_bonus", 0)
                    self.game.display(5)
                elif self.return_button.get_rect(x=750, y=725).collidepoint(*evt.pos):
                    self.game.display(4)
                self.focus = False
