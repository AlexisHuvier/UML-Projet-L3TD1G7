from src.tiles.Tile import Tile


class GreyTile(Tile):
    img="G"
    
    def __init__(self):
        print("tile")
        
    def __str__(self):
        return "G affichage"

    def can_go(self,Personnage):
        return False

    def display():
        print(img)
    
    def apply(personnage):
        print("effect")
