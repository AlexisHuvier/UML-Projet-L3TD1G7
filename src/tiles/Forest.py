from src.tiles.Tile import Tile
import random

class Forest(Tile):
    def __init__(self, position):
        super(Forest, self).__init__(position, "files/images/tiles/forest.png")

    def __str__(self):
        return "F"

    def can_go(self,personnage):
        if(personnage.movement_mode != 0): # Passe le personnage à pied s'il ne l'est pas déjà
            print("A pied")
            personnage.movement_mode = 0
        return True

    def apply(self,personnage):
        r=random.uniform(0, 1)
        if (r<=0.1):
            personnage.life-=10
            print("Le personnage a eu une maladie")
