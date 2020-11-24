
import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        random_number = random.randint((int(self.max_damage) // 2), int(self.max_damage))
        return random_number