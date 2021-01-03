from src.tiles.Tile import Tile


class GreyTile(Tile):
    def __init__(self, position):
        super(GreyTile, self).__init__(position, "files/images/tiles/gray.png")

    def __str__(self):
        return "G"

    def can_go(self,personnage):
        return False
