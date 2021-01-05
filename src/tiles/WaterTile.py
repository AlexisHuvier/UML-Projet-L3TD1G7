from src.tiles.Tile import Tile
import random

class WaterTile(Tile):
    def __init__(self, position):
        super(WaterTile, self).__init__(position, "files/images/tiles/water.png")

    def __str__(self):
        return "W"

    def can_go(self,personnage):
        if personnage.has_swimsuit:
            personnage.movement_mode = 0
            return True
        return False

    def apply(self,personnage):
        r=random.uniform(0, 1)
        if (r<=0.05):
            personnage.life-=10
