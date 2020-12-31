from src.tiles.buildings.Building import Building
import random

class Pub(Building):
    """
    classe pub
    """
    def __init__(self):
        """Constructeur de notre classe"""
        super()
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BP"

    def apply(self,personnage):
        p=random.randint(0,100)
        personnage.hydration+=25
        personnage.mentality+=25
        if (personnage.mentality>100):
            personnage.mentality=100
        if (personnage.hydration>100):
            personnage.hydration=100
        personnage.life-=3
        if (p>=5):
            personnage.diplomaObtainingBonus+=5
