import random

from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:

  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()

    self.deaths = 0
    self.kills = 0
    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def add_weapon(self, weapon):
    '''Add weapon to self.abilities'''
    # TODO: This method will append the weapon object passed in as an
    # argument to self.abilities.
    # This means that self.abilities will be a list of
    # abilities and weapons.
    self.abilities.append(weapon)

  def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in. '''
    # TODO: Fight each hero until a victor emerges.
    # Phases to implement:
    #1) randomly choose winner,
    #Hint: Look into random library, more specifically the choice method
    if len(self.abilities) == 0 and len(opponent.abilies) == 0:
      print(f"draw")
    else: #if hero has ability
      while self.is_alive() and opponent.is_alive():
        opponent.take_damage(self.attack())
        self.take_damage(opponent.attack())
        if self.is_alive() == False:
          print(f"{opponent.name} wins!")
          self.add_death(1)
          opponent.add_kill(1)
        elif opponent.is_alive() == False:
          self.add_kill(1)
          opponent.add_death(1)
          print(f"{self.name} wins!")

  def add_kill(self, num_kills):
    ''' Update self.kills by num_kills amount'''
    self.kills += num_kills

  def add_death(self, num_deaths):
    ''' Update deaths with num_deaths'''
    # TODO: This method should add the number of deaths to self.deaths
    self.deaths += num_deaths

  def add_ability(self, ability):
    ''' Add ability to abilities list '''

    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)

  def attack(self):
    '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
    '''

    # start our total out at 0
    total_damage = 0
    # loop through all of our hero's abilities
    for ability in self.abilities:
        # add the damage of each attack to our running total
        total_damage += ability.attack()
    # return the total damage
    return total_damage

  def add_armor(self, armor):
    '''Add armor to self.armors
      Armor: Armor Object
    '''
    # TODO: Add armor object that is passed in to `self.armors`
    self.armors.append(armor)

  def defend(self):
    '''Calculate the total block amount from all armor blocks.
      return: total_block:Int
    '''
    # TODO: This method should run the block method on each armor in self.armors
    total_block = 0
    # loop through all of our hero's armors
    for armor in self.armors:
        # add the block of each block to our running total
        total_blocks += armor.defend()
    # return the total block
    return total_block

  def take_damage(self, damage):
    '''Updates self.current_health to reflect the damage minus the defense.
    '''
    # TODO: Create a method that updates self.current_health to the current
    # minus the the amount returned from calling self.defend(damage).
    self.current_health = self.current_health - damage

  def is_alive(self):  
    '''Return True or False depending on whether the hero is alive or not.
    '''
    # TODO: Check the current_health of the hero.
    # if it is <= 0, then return False. Otherwise, they still have health
    # and are therefore alive, so return True
    if self.current_health <= 0:
        return False
    else:
        return True


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())