from src.tiles.buildings.Building import Building
import random

class University(Building):
    """
    classe University
    """
    def __init__(self, position):
        super(University, self).__init__(position, "files/images/tiles/university.png")

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BU"

    def apply(self,personnage):
        p=random.randint(0,100)
        if (p<=30+personnage.diplomaObtainingBonus):
            personnage.diplomaCounter+=1
            personnage.mentality+=5
            if (personnage.mentality>100):
                personnage.mentality=100
        personnage.diplomaObtainingBonus=0
