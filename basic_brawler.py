import pygame,sys,time
from enum import Enum

# All possible states a character can be in

class State(Enum):
    IDLE = "idle"
    SHIELDING = "shielding"
    SHIELD_BROKEN = "shield_broken"
    ATTACKING = "attacking"
    HURT = "hurt"

class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, char_name, image_path, x, y, groups):
        super().__init__(groups)

        self.char_name = char_name

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))#image loading and starting position
        self.max_health = 100
        self.health = self.max_health#boring health stuff
        self.gravity = 0 
        self.gravity_strength = 1 #boring gravity stuff
        self.ground_level = 700 # where the floor is
        self.attack_mod = 1.0# cuz this is the parent class it is one but it is an attack mult
        self.state = State.IDLE # starting tate is doing nothing
        self.state_start_time = 0 #we need a starting point for the later states to ovveride so we just bs one
        self.shield_hits_remaining = 2 #max hits of the shield basically
        self.SHIELD_DURATION = 4000      # 4 seconnds for how long the shield will live
        self.SHIELD_BREAK_ENDLAG = 3000  # 3 seconds of endlag once the shield breaks

    def grav(self):
        self.gravity += 1
        self.rect.y = self.gravity
        if self.rect.bottom == 700:
            self.rect.bottom = 700
            self.gravity = 0

    def damage_taken(self,incoming_damage):
        damage = max(0, incoming_damage - self.shield)
        self.health = max(0, self.health - damage)

    def punch(self):
        return self.attack_mod 
    
    def kick(self):
        return self.attack_mod

    def shield(self):
        self.print('dd')

    def hitsun(self):
        self.Print('67')



















