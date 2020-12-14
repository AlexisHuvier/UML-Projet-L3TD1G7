from src.tiles.Tile import Tile
import random

class Forest(Tile):
    img="F"
    
    def __init__(self):
        print("tile")
        
    def __str__(self):
        return "F affichage"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" or personnage.movement_mode=="bicycle"):
            return True
        return False

    def display():
        print(img)
    
    def apply(self,personnage):
        print("effect")
        r=random.uniform()
        if (r<=0.1):
            personnage.life-=10
        
        
