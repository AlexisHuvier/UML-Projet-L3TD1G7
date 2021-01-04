from src.tiles.Tile import Tile
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
                    personnage.applyRedTrafficLight()
                elif (p==1):
                    personnage.applyPolice()
                else:
                    personnage.applyPotHole()


##        if (r<=0.02):
##            personnage.life-=100
##        r=random.uniform(0, 1)
##        if (r<=0.05):
##            personnage.arrest_count+=1
##            if (personnage.arrest_count>=3):
##                personnage.life-=100
