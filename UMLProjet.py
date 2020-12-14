import pygame
import sys

from src.menus import *

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
        self.current_displayed = 4

        self.clock = pygame.time.Clock()
        self.is_running = False

    def stop(self):
        self.is_running = False

    def display(self, new):
        self.current_displayed = new

    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if(self.current_displayed < len(self.screens)):
                self.screens[self.current_displayed].process_event(evt)

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill((0, 0, 0))

            if(self.current_displayed < len(self.screens)):
                self.screens[self.current_displayed].display(self.screen)

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