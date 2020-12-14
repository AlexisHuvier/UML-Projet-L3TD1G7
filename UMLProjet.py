import pygame
import sys

from src.menus import *
from src.character import Hippy, HurriedMan, Standard

pygame.init()

class UMLProjet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
        self.width = 900
        self.height = 600

        pygame.display.set_caption("UMLProjet")
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screens = [MainMenu(self), CharacterMenu(self), LoadMenu(self), SaveMenu(self), PauseMenu(self)]
        self.current_displayed = 0

        self.player = None
        self.pause_button = pygame.Surface((100, 40), pygame.SRCALPHA, 32).convert_alpha()
        self.pause_button.fill((50, 50, 50))
        pause_title = pygame.font.SysFont("Arial", 16).render("Pause", True, (255, 255, 255))
        pause_size = pygame.font.SysFont("Arial", 16).size("Pause")
        self.pause_button.blit(pause_title, (50 - pause_size[0]/2, 20 - pause_size[1]/2))

        self.clock = pygame.time.Clock()
        self.is_running = False

    def stop(self):
        self.is_running = False

    def display(self, new):
        self.current_displayed = new
    
    def create_player(self, type_):
        if type_ == 0:
            self.player = Standard(self, (100, 100), (0, 0), 0, False, 0)
        elif type_ == 1:
            self.player = Hippy(self, (100, 100), (0, 0), 0, False, 0)
        else:
            self.player = HurriedMan(self, (100, 100), (0, 0), 0, False, 0)

    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if(self.current_displayed < len(self.screens)):
                self.screens[self.current_displayed].process_event(evt)
            else:
                if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                    if self.pause_button.get_rect(x=750, y=50).collidepoint(*evt.pos):
                        self.display(4)

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill((0, 0, 0))

            if(self.current_displayed < len(self.screens)):
                self.screens[self.current_displayed].display(self.screen)
            else:
                self.player.display(self.screen)
                self.screen.blit(self.pause_button, (750, 50))

            self.clock.tick()
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        n = 10
        m = 10
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        except ValueError:
            print("Error : Width and height must be integer")
            n = 10
            m = 10
    project = UMLProjet(n, m)
    project.run()