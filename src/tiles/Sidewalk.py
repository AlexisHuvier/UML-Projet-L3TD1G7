from src.tiles.Tile import Tile
import random


class Sidewalk(Tile):
    def __init__(self, position):
        super(Sidewalk, self).__init__(position, "files/images/tiles/sidewalk.png")

    def __str__(self):
        return "S"

    def can_go(self,personnage):
        return personnage.movement_mode==0

    def apply(self, personnage):
        if (personnage.movement_mode==0):
            p=random.randint(0,100)
            if (p<=5):
                p=random.randint(0,2)
                if (p==0):
                    Trap.applyBananaPeel(personnage)
                elif (p==1):
                    Trap.applyPoo(personnage)
                else:
                    Trap.applyStroller(personnage)


##        if (r<=0.02):
##            personnage.life-=100
##        r=random.uniform()
##        if (r<=0.05):
##            personnage.arrest_count+=1
##            if (personnage.arrest_count>=3):
##                personnage.life-=100
