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
        self.dead = False

    def __str__(self):
        return self.__class__.__name__+"(L:{}, H:{}, S:{}, M:{}, P:{}, GP:{}, MM:{}, HS:{}, AC:{}, DC:{}, DOB:{})".format(self.life, self.hydration, self.satiety, self.mentality, self.position, self.go_position, self.movement_mode, self.has_swimsuit, self.arrest_count, self.diplomaCounter, self.diplomaObtainingBonus)

    def move(self):
        moving = False
        if not self.dead:
            if self.life <= 0 or self.satiety <= 0 or self.hydration <= 0 or self.mentality <= 0:
                print(self)
                print("Le personnage est mort")
                self.dead = True
            elif self.arrest_count >= 3:
                print(self)
                print("Le personnage a fini en prison")
                self.dead = True
            else:
                if self.position[0] < self.go_position[0] and self.game.map.get_case((self.position[0]+1, self.position[1])).can_go(self): # Se déplace à droite
                    self.position[0] += 1
                    self.game.map.get_case(self.position).apply(self)
                    moving = True
                elif self.position[0] > self.go_position[0] and self.game.map.get_case((self.position[0]-1, self.position[1])).can_go(self): # Se déplace à gauche
                    self.position[0] -= 1
                    self.game.map.get_case(self.position).apply(self)
                    moving = True
                elif self.position[1] < self.go_position[1] and self.game.map.get_case((self.position[0], self.position[1]+1)).can_go(self): # Se déplace en bas
                    self.position[1] += 1
                    self.game.map.get_case(self.position).apply(self)
                    moving = True
                elif self.position[1] > self.go_position[1] and self.game.map.get_case((self.position[0], self.position[1]-1)).can_go(self): # Se déplace en haut
                    self.position[1] -= 1
                    self.game.map.get_case(self.position).apply(self)
                    moving = True

                if moving:
                    from src.tiles.buildings import Building
                    if not issubclass(self.game.map.get_case(self.position).__class__, Building): # Si on est pas sur un batiment, on applique les effets des modes de déplacement
                        from src.Movement import Movement
                        if self.movement_mode == 0:
                            Movement.applyFoot(self)
                        elif self.movement_mode == 1:
                            Movement.applyBike(self)
                        else:
                            Movement.applyCar(self)
        return moving
            

    def display(self, screen):
        screen.blit(self.sprite, (self.position[0]*64, self.position[1]*64))

class Standard(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(75, 75, 75, 75, "files/images/standard.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)

    def move(self):
        if super(Standard, self).move(): # Si le personnage ne bouge pas, on n'applique pas les effets de déplacements
            self.life -= 1
            self.hydration -= 1
            self.satiety -= 1
            self.mentality -= 1
            print(self)
        

class Hippy(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(75, 50, 50, 100, "files/images/hippie.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)

    def move(self):
        if super(Hippy, self).move(): # Si le personnage ne bouge pas, on n'applique pas les effets de déplacements
            self.life -= 0.5
            self.hydration -= 0.5
            self.satiety -= 0.5
            print(self)

class HurriedMan(Character):

    def __init__(self, game, position, go_position, movement_mode, has_swimsuit, arrest_count):
        super().__init__(100, 75, 75, 50, "files/images/presse.png", game, position, go_position, movement_mode, has_swimsuit, arrest_count)

    def move(self):
        if super(HurriedMan, self).move(): # Si le personnage ne bouge pas, on n'applique pas les effets de déplacements
            self.life -= 1
            self.hydration -= 1
            self.satiety -= 1
            self.mentality -= 1
            print(self)
        
