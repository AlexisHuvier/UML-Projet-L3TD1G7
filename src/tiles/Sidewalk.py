from src.tiles.Tile import Tile


class Sidewalk(Tile):
    img="S"
    

        
    def __str__(self):
        return "S"

    def can_go(self,Personnage):
        if (personnage.movement_mode=="feet"):
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
        
