from src.tiles.Tile import Tile


class Road(Tile):
    img="R"
    
    def __init__(self):
        print("tile")
        
    def __str__(self):
        return "R affichage"

    def can_go(self,Personnage):
        if (personnage.movement_mode=="car" or personnage.movement_mode=="bicycle"):
            return True
        return False

    def display():
        print(img)
    
    def apply(personnage):
        print("effect")
        r=random.uniform()
        if (r<=0.05):
            personnage.life-=10
        r=random.uniform()
        if (r<=0.05):
            r=random.randint(0,2)
            if (r==0):
                print("piege1")
            elif (r==1):
                print("piege2")
            else:
                print("piege3")

        
##        if (r<=0.02):
##            personnage.life-=100
##        r=random.uniform()
##        if (r<=0.05):
##            personnage.arrest_count+=1
##            if (personnage.arrest_count>=3):
##                personnage.life-=100
        
