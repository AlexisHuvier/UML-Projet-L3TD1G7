import pygame
import sys

from src.menus import *
from src.Character import Hippy, HurriedMan, Standard
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
        self.screen = pygame.display.set_mode((self.width, self.height)) # Création de l'écran

        self.screens = [MainMenu(self), CharacterMenu(self), LoadMenu(self), SaveMenu(self), PauseMenu(self)] # Liste des menus
        self.current_displayed = 0 # Affiche par défaut le menu d'id 0 soit le menu Principal

        self.player = None

        self.clock = pygame.time.Clock()
        self.is_running = False
        self.time_move = 30

    def stop(self):
        self.is_running = False

    def display(self, new):
        self.current_displayed = new # Change le menu affiché (ou le jeu)
    
    def create_player(self, type_):
        posBuildings = self.map.generateMap(self.n, self.m)
        if type_ == 0:
            self.player = Standard(self, posBuildings["House"], posBuildings["House"], 0, False, 0)
        elif type_ == 1:
            self.player = Hippy(self, posBuildings["House"], posBuildings["House"], 0, False, 0)
        else:
            self.player = HurriedMan(self, posBuildings["House"], posBuildings["House"], 0, False, 0)
        print("NEW GAME")
        print(self.player)

    def process_event(self, evt):
        if evt.type == pygame.QUIT:
            self.stop()
        else:
            if(self.current_displayed < len(self.screens)): # Si le menu affiché est dans la liste des menus alors on lui passe les évènements
                self.screens[self.current_displayed].process_event(evt)
            else:
                if evt.type == pygame.KEYDOWN: # Sinon, c'est le jeu et on traite les évènements
                    if evt.key == pygame.K_p:
                        self.display(4)
                    elif evt.key == pygame.K_LEFT:
                        if self.player.position[0] > 0:
                            self.player.go_position = (self.player.position[0] - 1, self.player.position[1])
                    elif evt.key == pygame.K_RIGHT:
                        if self.player.position[0] < self.n - 1:
                            self.player.go_position = (self.player.position[0] + 1, self.player.position[1])
                    elif evt.key == pygame.K_UP:
                        if self.player.position[1] > 0:
                            self.player.go_position = (self.player.position[0], self.player.position[1] - 1)
                    elif evt.key == pygame.K_DOWN:
                        if self.player.position[1] < self.m - 1:
                            self.player.go_position = (self.player.position[0], self.player.position[1] + 1)

    def run(self):
        self.is_running = True
        while self.is_running: # Boucle principale de jeu
            for event in pygame.event.get():
                self.process_event(event)
            
            self.screen.fill((0, 0, 0)) # Remplit l'écran de noir

            if(self.current_displayed < len(self.screens)): # Si le menu affiché est dans la liste des menus alors on l'affiche
                self.screens[self.current_displayed].display(self.screen)
            else: # Sinon, on affiche le jeu (donc la map, le personnage) et on déplace le personnage
                self.map.display(self.screen)
                self.player.display(self.screen)
                self.time_move -= 1
                if self.time_move == 0:
                    self.player.move()
                    self.time_move = 30

            self.clock.tick(60) # On bloque à 60 fps (60 updates par secondes)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3: 
        n = 5
        m = 5
    else:
        try:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        except ValueError:
            print("Error : Width and height must be integer")
            n = 5
            m = 5
    project = UMLProjet(n, m)
    project.run()