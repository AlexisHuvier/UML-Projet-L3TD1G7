from src.Character import *

class Trap:

    @classmethod
    def applyRedTrafficLight(cls, character):
        print("Le personnage s'est pris un feu rouge")
        character.life -= 1

    @classmethod
    def applyPolice(cls, character):
        print("Le personnage a rencontre la police")
        if(not isinstance(character, Hippy)):
            character.mentality -= 1

    @classmethod
    def applyPothole(cls, character):
        print("Le personnage a roule dans un nid de poule")
        character.hydration -= 2
        character.satiety -= 2

    @classmethod
    def applyBananaPeel(cls, character):
        print("Le personnage a marche sur une peau de banane")
        character.life -= 3

    @classmethod
    def applyStroller(cls, character):
        print("Le personnage est derriere une poussette")
        if(not isinstance(character, Hippy)):
            character.mentality -= 2

    @classmethod
    def applyPoo(cls, character):
        print("Le personnage a marche dans une crotte")
        character.satiety -= 1