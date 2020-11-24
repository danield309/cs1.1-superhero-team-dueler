import random 
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()
        self.deaths = 0
        self.kills = 0
    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        total_defend = 0
        for armor in self.armor:
            total_defend -= armor.block()
        return total_defend

    def take_damage(self, damage):
        damage_taken = damage - self.defend()
        if damage_taken > 0:
            self.current_health -= damage_taken
    
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):  
        
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
            return

        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == True:
                print(f"{self.name} wins!")
            elif opponent.is_alive() == True:
                print(f"{opponent.name} wins!")

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_kill(self, num_kills):
        self.kills += num_kills 

    def add_death(self, num_deaths):
        self.deaths += num_deaths
    


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
