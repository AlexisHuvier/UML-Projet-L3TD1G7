from src.tiles.buildings.Building import Building


class House(Building):
    """
    classe House
    """
    def __init__(self, position):
        super(House, self).__init__(position, "files/images/tiles/house.png")

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BH"

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
