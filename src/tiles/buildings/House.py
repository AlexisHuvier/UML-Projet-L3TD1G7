from src.tiles.buildings.Building import Building


class House(Building):
    """
    classe House
    """
    self.sprite = pygame.image.load(sprite)
    def __init__(self):
        """Constructeur de notre classe"""
        super()

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BH"

    def display(self, screen):
        screen.blit(self.sprite, self.position)

    def apply(self,personnage):
        personnage.mentality=personnage.mentality+10
        personnage.hydration=personnage.hydration+10
        personnage.satiety=personnage.satiety+10
        if (personnage.mentality>100):
            personnage.mentality=100
        if (personnage.hydration>100):
            personnage.hydration=100
        if (personnage.satiety>100):
            personnage.satiety=100
