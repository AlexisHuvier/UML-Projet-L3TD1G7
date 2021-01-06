from src.tiles.Tile import Tile
from src.Trap import Trap
from src.Character import Hippy, Standard, HurriedMan
import random

class Road(Tile):
    def __init__(self, position):
        super(Road, self).__init__(position, "files/images/tiles/road.png")

    def __str__(self):
        return "R"

    def can_go(self,personnage):
        if(personnage.movement_mode==0):
            p = random.uniform(0,1)
            if(isinstance(personnage, Hippy) or (isinstance(personnage, Standard) and p<0.4) or (isinstance(personnage, HurriedMan) and p<0.1)):
                # Fait passer le personnage en vélo s'il est un Hippie ou avec 40% de chance s'il est un Standard ou 10% de chance s'il est un Homme Pressé
                personnage.movement_mode = 1
                print("En velo")
            else:
                # Sinon le personnage passe en voiture
                personnage.movement_mode = 2
                print("En voiture")
        return True

    def apply(self, personnage):
        if (personnage.movement_mode==2 or personnage.movement_mode==1):
            p=random.randint(0,100)
            if (p<=5):
                p=random.randint(0,2)
                if (p==0):
                    Trap.applyRedTrafficLight(personnage)
                elif (p==1):
                    Trap.applyPolice(personnage)
                else:
                    Trap.applyPothole(personnage)