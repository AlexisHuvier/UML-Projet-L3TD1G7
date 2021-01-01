from src.tiles.Tile import Tile


class Sidewalk(Tile):
    def __init__(self, position):
        super(Sidewalk, self).__init__(position, "files/images/tiles/sidewalk.png")

    def __str__(self):
        return "S"

    def can_go(self,Personnage):
        if (personnage.movement_mode=="feet"):
            return True
        return False

    def apply(personnage):
        if (personnage.movement_mode=="feet"):
            p=random.randint(0,100)
            if (p<=5):
                p=random.randint(0,2)
                if (p==0):
                    personnage.applyPeauBanane()
                elif (p==1):
                    personnage.applyDejectionCanine()
                else:
                    personnage.applyPoussette()


##        if (r<=0.02):
##            personnage.life-=100
##        r=random.uniform()
##        if (r<=0.05):
##            personnage.arrest_count+=1
##            if (personnage.arrest_count>=3):
##                personnage.life-=100
