class Character:

    def __init__(self, life, hydration, satiety, mentality, sprite, game, position, go_position, movement_mode, has_swimsuit):
        self.life = life
        self.hydration = hydration
        self.satiety = satiety
        self.mentality = mentality
        self.sprite = sprite
        self.game = game                                # Liaison entre la ville et le personnage
        self.position = position                        # Position x et y courante
        self.go_position = go_position                  # Position x et y suivante
        self.movement_mode = movement_mode
        self.has_swimsuit = has_swimsuit

    def move(self):
        pass

    def display(self, screen):
        pass

class Standard(Character):

    def __init__(self, sprite, game, position, go_position, movement_mode, has_swimsuit):
        super().__init__(75, 75, 75, 75, sprite, game, position, go_position, movement_mode, has_swimsuit)
    
    def move(self):
        self.life -= 1
        self.hydration -= 1
        self.satiety -= 1
        self.mentality -= 1


class Hippy(Character):

    def __init__(self, sprite, game, position, go_position, movement_mode, has_swimsuit):
        super().__init__(75, 50, 50, 100, sprite, game, position, go_position, movement_mode, has_swimsuit)
    
    def move(self):
        self.life -= 2
        self.hydration -= 2
        self.satiety -= 2

class HurriedMan(Character):

    def __init__(self, sprite, game, position, go_position, movement_mode, has_swimsuit):
        super().__init__(100, 75, 75, 50, sprite, game, position, go_position, movement_mode, has_swimsuit)
    
    def move(self):
        self.mentality -= 2