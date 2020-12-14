from src.tiles.buildings.Building import Building

class Library(Building):
    """
    classe Library
    """
    def __init__(self):
        """Constructeur de notre classe"""
        super()
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "BL"