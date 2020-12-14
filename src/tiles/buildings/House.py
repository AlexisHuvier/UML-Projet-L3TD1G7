from src.tiles.buildings.Building import Building


class House(Building):
    """
    classe House
    """
    def __init__(self):
        """Constructeur de notre classe"""
        super()

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BH"
