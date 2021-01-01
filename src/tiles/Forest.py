from src.tiles.Tile import Tile
import random

class Forest(Tile):
    img="F"
    self.sprite = pygame.image.load(sprite)

    def __str__(self):
        return "F"

    def can_go(self,personnage):
        if (personnage.movement_mode=="foot" or personnage.movement_mode=="bicycle"):
            return True
        return False

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        r=random.uniform()
        if (r<=0.1):
            personnage.life-=10
