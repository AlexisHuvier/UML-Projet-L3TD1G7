from src.tiles.Tile import Tile

class Building(Tile):
    """
    classe batiment
    """
    def __init__(self):
        """Constructeur de notre classe"""
        print("building")
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "building affichage"

    def can_go(self,personnage):
        return True

    def display():
        print(img)

    def apply(self,personnage):
        print("effect")
