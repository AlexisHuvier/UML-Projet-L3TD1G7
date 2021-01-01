from src.tiles.Tile import Tile

class Building(Tile):
    """
    classe batiment
    """
    self.sprite = pygame.image.load(sprite)

    def __init__(self):
        """Constructeur de notre classe"""
        print("building")
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "building affichage"

    def can_go(self,personnage):
        return True

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        print("effect")
