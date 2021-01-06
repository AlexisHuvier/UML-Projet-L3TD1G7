from src.tiles.buildings.Building import Building
import random

class Library(Building):
    """
    classe Library
    """
    def __init__(self, position):
        super(Library, self).__init__(position, "files/images/tiles/library.png")

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BL"

    def apply(self,personnage):
        p=random.randint(0,100)
        personnage.mentality+=20
        if (personnage.mentality>100):
            personnage.mentality=100
        if (p<=5):
            print("Le personnage a trouve un livre sur le GL")
            personnage.diplomaObtainingBonus+=10
