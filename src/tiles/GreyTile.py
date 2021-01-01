from src.tiles.Tile import Tile


class GreyTile(Tile):
    img="G"
    self.sprite = pygame.image.load(sprite)

    def __str__(self):
        return "G"

    def can_go(self,Personnage):
        return False

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(personnage):
        print("effect")
