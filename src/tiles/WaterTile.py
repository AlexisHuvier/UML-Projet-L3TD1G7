from src.tiles.Tile import Tile


class WaterTile(Tile):
    img="W"
    self.sprite = pygame.image.load(sprite)


    def __str__(self):
        return "W"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" and personnage.has_swimsuit==True):
            return True
        return False

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        print("effect")
        r=random.uniform()
        if (r<=0.05):
            personnage.life-=10
