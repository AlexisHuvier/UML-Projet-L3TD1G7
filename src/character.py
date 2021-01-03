import pygame

class Character:

    def __init__(self, life, hydration, satiety, mentality, sprite, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        self.life = life
        self.hydration = hydration
        self.satiety = satiety
        self.mentality = mentality
        self.sprite = pygame.transform.scale2x(pygame.image.load(sprite))
        self.game = game                                # Liaison entre la ville et le personnage
        self.position = position                        # Position x et y courante
        self.go_position = go_position                  # Position x et y suivante
        self.movement_mode = movement_mode
        self.has_swimsuit = has_swimsuit
        self.arrest_count = arrest_count
        self.diplomaCounter = 0
        self.diplomaObtainingBonus = 0

    def __str__(self):
        return self.__class__.__name__+"(L:{}, H:{}, S:{}, M:{}, P:{}, GP:{}, MM:{}, HS:{}, AC:{}, DC:{}, DOB:{})".format(self.life, self.hydration, self.satiety, self.mentality, self.position, self.go_position, self.movement_mode, self.has_swimsuit, self.arrest_count, self.diplomaCounter, self.diplomaObtainingBonus)

    def move(self):
        pass

    def display(self, screen):
        screen.blit(self.sprite, self.position)

class Standard(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(75, 75, 75, 75, "files/images/standard.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)
    
    def move(self):
        self.life -= 1
        self.hydration -= 1
        self.satiety -= 1
        self.mentality -= 1


class Hippy(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(75, 50, 50, 100, "files/images/hippie.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)
    
    def move(self):
        self.life -= 0.5
        self.hydration -= 0.5
        self.satiety -= 0.5

class HurriedMan(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(100, 75, 75, 50, "files/images/presse.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)
    
    def move(self):
        self.life -= 1
        self.hydration -= 1
        self.satiety -= 1
        self.mentality -= 1