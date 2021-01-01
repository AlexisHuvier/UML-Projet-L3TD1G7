from src.tiles.buildings.Building import Building

class FastFood(Building):
    """
    classe fast food
    """
    def __init__(self, position):
        super(FastFood, self).__init__(position, "files/images/tiles/fastfood.png")

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BF"
        
    def apply(self,personnage):
        personnage.mentality=personnage.mentality+10
        personnage.hydration=personnage.hydration+10
        personnage.satiety=personnage.satiety+25
        personnage.life=personnage.life-5
        if (personnage.mentality>100):
            personnage.mentality=100
        if (personnage.hydration>100):
            personnage.hydration=100
        if (personnage.satiety>100):
            personnage.satiety=100
