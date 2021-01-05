from src.tiles.Tile import Tile

class Building(Tile):
    """
    classe batiment
    """
    def __init__(self, position, sprite):
        super(Building, self).__init__(position, sprite)
        
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "building affichage"

    def can_go(self,personnage):
        personnage.movement_mode = 0
        return True
