from src.tiles.Tile import Tile
import random

class Forest(Tile):
    def __init__(self, position):
        super(Forest, self).__init__(position, "files/images/tiles/gray.png")

    def __str__(self):
        return "F"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" or personnage.movement_mode=="bicycle"):
            return True
        return False

    def apply(self,personnage):
        r=random.uniform()
        if (r<=0.1):
            personnage.life-=10
