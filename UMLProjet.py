import pygame
import sys

from src.menus import MainMenu

pygame.init()

class UMLProjet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
        self.width = 900
        self.height = 600

        pygame.display.set_caption("UMLProjet")
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.menus = [MainMenu(self)]
        self.current_showed = 0

        self.clock = pygame.time.Clock()
        self.is_running = False

    def stop(self):
        self.is_running = False

    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if(self.current_showed < len(self.menus)):
                self.menus[self.current_showed].process_event(evt)

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill((0, 0, 0))

            if(self.current_showed < len(self.menus)):
                self.menus[self.current_showed].display(self.screen)

            self.clock.tick()
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python "+sys.argv[0]+" <width> <height>")
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
            project = UMLProjet(n, m)
            project.run()
        except ValueError:
            print("Error : Width and height must be integer")