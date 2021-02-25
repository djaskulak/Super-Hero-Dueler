import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in. '''
      # TODO: Fight each hero until a victor emerges.
      # Phases to implement:
      #1) randomly choose winner,
      #Hint: Look into random library, more specifically the choice method
      heros = [self, opponent]
      
      winner = random.choice(heros)
      print(winner.name + " won!")
    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)