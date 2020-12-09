class Character:

    def __init__(self, life, hydration, satiety, mentality, sprite, position, go_position):
        self.life = life
        self.hyration = hydration
        self.satiety = satiety
        self.mentality = mentality
        self.sprite = sprite
        self.position = position                        # Position x et y courante
        self.go_position = go_position                  # Position x et y suivante

        def move():
            pass