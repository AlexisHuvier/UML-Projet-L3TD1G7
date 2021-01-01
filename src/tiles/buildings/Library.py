from src.tiles.buildings.Building import Building
import random

class Library(Building):
    """
    classe Library
    """
    self.sprite = pygame.image.load(sprite)
    def __init__(self):
        """Constructeur de notre classe"""
        super()
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BL"

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        p=random.randint(0,100)
        personnage.mentality+=20
        if (personnage.mentality>100):
            personnage.mentality=100
        if (p<=5):
            personnage.diplomaObtainingBonus+=10
