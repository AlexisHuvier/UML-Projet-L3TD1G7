from src.Character import *

class Trap:

    @classmethod
    def applyRedTrafficLight(cls, character):
        character.life -= 1

    @classmethod
    def applyPolice(cls, character):
        if(not isinstance(character, Hippy)):
            character.mentality -= 1

    @classmethod
    def applyPothole(cls, character):
        character.hydration -= 2
        character.satiety -= 2

    @classmethod
    def applyBananaPeel(cls, character):
        character.life -= 3

    @classmethod
    def applyStroller(cls, character):
        if(not isinstance(character, Hippy)):
            character.mentality -= 2

    @classmethod
    def applyPoo(cls, character):
        character.satiety -= 1