import pygame
import sys

from src.menus import *
from src.character import Hippy, HurriedMan, Standard
from src.tiles import Map

pygame.init()

class UMLProjet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
        self.width = 1200
        self.height = 900
        self.map = Map()

        pygame.display.set_caption("UMLProjet")
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.screens = [MainMenu(self), CharacterMenu(self), LoadMenu(self), SaveMenu(self), PauseMenu(self)]
        self.current_displayed = 0

        self.player = None

        self.clock = pygame.time.Clock()
        self.is_running = False

    def stop(self):
        self.is_running = False

    def display(self, new):
        self.current_displayed = new
    
    def create_player(self, type_):
        posHouse = self.map.generateMap()
        if type_ == 0:
            self.player = Standard(self, [posHouse[0]*64, posHouse[1]*64], (0, 0), 0, False, 0)
        elif type_ == 1:
            self.player = Hippy(self, [posHouse[0]*64, posHouse[1]*64], (0, 0), 0, False, 0)
        else:
            self.player = HurriedMan(self, [posHouse[0]*64, posHouse[1]*64], (0, 0), 0, False, 0)

    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if(self.current_displayed < len(self.screens)):
                self.screens[self.current_displayed].process_event(evt)
            else:
                if evt.type == pygame.KEYDOWN and evt.key == pygame.K_p:
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
                self.map.display(self.screen)
                self.player.display(self.screen)

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