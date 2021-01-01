from src.tiles.Tile import Tile


class Road(Tile):
    def __init__(self, position):
        super(Road, self).__init__(position, "files/images/tiles/road.png")

    def __str__(self):
        return "R"

    def can_go(self,Personnage):
        if (personnage.movement_mode=="car" or personnage.movement_mode=="bicycle"):
            return True
        return False

    def apply(personnage):
        if (personnage.movement_mode=="car" or personnage.movement_mode=="bicycle"):
            p=random.randint(0,100)
            if (p<=5):
                p=random.randint(0,2)
                if (p==0):
                    personnage.applyFeuRouge()
                elif (p==1):
                    personnage.applyPolice()
                else:
                    personnage.applyNidPoule()


##        if (r<=0.02):
##            personnage.life-=100
##        r=random.uniform()
##        if (r<=0.05):
##            personnage.arrest_count+=1
##            if (personnage.arrest_count>=3):
##                personnage.life-=100
