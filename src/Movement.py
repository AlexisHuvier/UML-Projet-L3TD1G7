from src.Character import Standard, Hippy, HurriedMan
from random import *

class Movement:

    @classmethod
    def applyFoot(cls, character): # Déplacement à pied
        if(isinstance(character, Standard)):
            character.hydration -= 10
            character.satiety -= 10
        elif(isinstance(character, Hippy)):
            character.hydration -= 20
            character.satiety -= 20
        elif(isinstance(character, HurriedMan)):
            character.mentality -= 2
    
    @classmethod
    def applyCar(cls, character): # Déplacement en voiture
            character.mentality -= 2
        p_death = uniform(0,1)
        if(p_death <= 0.02):
            character.life = 0
            print("Le personnage a eu un accident")
        p_arrest = uniform(0,1)
        if(p_arrest <= 0.05):
            character.arrest_count += 1
            print("Le personnage s'est fait arrêté")
        if(isinstance(character, HurriedMan)):
    
    @classmethod
    def applyBike(cls, character): # Déplacement à vélo
        p_death = uniform(0,1)
        if(p_death <= 0.005):
            character.life = 0
            print("Le personnage a eu un accident")
        if(isinstance(character, Standard)):
            character.hydration -= 5
            character.satiety -= 5
        elif(isinstance(character, Hippy)):
            character.hydration -= 10
            character.satiety -= 10
        elif(isinstance(character, HurriedMan)):
            character.mentality -= 2
    