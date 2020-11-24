import random
class Team:
    def __init__(self, name):
        
        self.name = name
        self.heroes = list()


    def remove_hero(self, name):

        foundHero = False

        for hero in self.heroes:
    
            if hero.name == name:
                self.heroes.remove(hero)
           
            foundHero = True
   
        if not foundHero:
            return 0
    def view_all_heroes(self):

        for hero in self.heroes:
            print(hero)
    
    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team):
        heroes_alive = list()
        opponents_alive = list()

        for hero in self.heroes:
            heroes_alive.append(hero)
        
        for hero in other_team.heroes:
            opponents_alive.append(hero)
        
        while len(heroes_alive) > 0 and len(opponents_alive) > 0:
            hero1 = random.choice(heroes_alive)
            hero2 = random.choice(opponents_alive)
            hero1.fight(hero2)
            
            if hero1.is_alive():
                heroes_alive.remove(hero2)
            
            elif hero2.is_alive():
                heroes_alive.remove(hero1)
            
            else:
                opponents_alive.remove(hero2)
                heroes_alive.remove(hero1)