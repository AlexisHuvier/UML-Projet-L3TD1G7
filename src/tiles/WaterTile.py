from src.tiles.Tile import Tile


class WaterTile(Tile):
    def __init__(self, position):
        super(WaterTile, self).__init__(position, "files/images/tiles/gray.png")

    def __str__(self):
        return "W"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" and personnage.has_swimsuit==True):
            return True
        return False

    def apply(self,personnage):
        print("effect")
        r=random.uniform()
        if (r<=0.05):
            personnage.life-=10
