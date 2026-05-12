class player_character:
    def __init__(self, char_name, app):
        """ Parent constructor - called before child constructors"""
        self.attack_mod = 1.0
        self.defense_mod = 1.0
        self.name = char_name
        self.shield = 0
        self.max_shield = 50
        self.y = 0
        self.x = 0
        self.app = app


class Brawler(player_character):


    def ___init___(self, char_name, app):
        player_character.___init___(self, char_name, app)
        self.max_health = 100;
        self.attack = 1.5;
        self.defense = 1;
        self.magic = 1;
        self.resistance = 10;
        self.health = self.max_health;


class Lil_baby(player_character):

    def ___init___(self, char_name, app):
        player_character.__init__(self, char_name, app)
        self.max_health = 80;
        self.attack = 0.3;
        self.defense = 0.3;
        self.magic = 5;
        self.resistance = 1;
        self.healtah = self.max_health;
















