from src.tiles.Tile import Tile
from src.Trap import Trap
import random

class Road(Tile):
    def __init__(self, position):
        super(Road, self).__init__(position, "files/images/tiles/road.png")

    def __str__(self):
        return "R"

    def can_go(self,personnage):
        return personnage.movement_mode==2 or personnage.movement_mode==1

    def apply(self, personnage):
        if (personnage.movement_mode==2 or personnage.movement_mode==1):
            p=random.randint(0,100)
            if (p<=5):
                p=random.randint(0,2)
                if (p==0):
                    Trap.applyRedTrafficLight(personnage)
                elif (p==1):
                    Trap.applyPolice(personnage)
                else:
                    Trap.applyPotHole(personnage)