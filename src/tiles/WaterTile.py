from src.tiles.Tile import Tile


class WaterTile(Tile):
    img="W"
    
    def __init__(self):
        print("tile")
        
    def __str__(self):
        return "W affichage"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" and personnage.has_swimsuit==True):
            return True
        return False

    def display():
        print(img)
    
    def apply(self,personnage):
        print("effect")
        r=random.uniform()
        if (r<=0.05):
            personnage.life-=10
