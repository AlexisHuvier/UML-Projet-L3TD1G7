import pygame


class Tile:
    """
    classe Tile
    """

    def __init__(self, position, sprite):
        self.sprite = pygame.image.load(sprite)
        self.position = position

    def __str__(self):
        return "tile affichage"

    def can_go(self,Personnage):
        return True

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        print("effect")
