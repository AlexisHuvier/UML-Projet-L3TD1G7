from Tile import *

class Building(Tile):
    """
    classe batiment
    """
    def __init__(self):
        """Constructeur de notre classe"""
        print("building")
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "building affichage"

    def apply():
        print("effect")
