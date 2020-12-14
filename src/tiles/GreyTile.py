from src.tiles.Tile import Tile


class GreyTile(Tile):
    img="G"
    
        
    def __str__(self):
        return "G"

    def can_go(self,Personnage):
        return False

    def display():
        print(img)
    
    def apply(personnage):
        print("effect")
