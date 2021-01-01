


class Tile:
    """
    classe Tile
    """
    img="T"
    self.sprite = pygame.image.load(sprite)

    def __str__(self):
        return "tile affichage"

    def can_go(self,Personnage):
        return True

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        print("effect")
