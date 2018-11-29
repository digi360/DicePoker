#class definition for an n-sided die

#import packages
from random import randint

class MSdie:

  sides = 0
  value = 0

  #constructor here
  def __init__(self, sides):
    self.sides = sides

  #define classmethod 'roll' to roll the MSdie
  def roll(self):
    self.value = randint(1, self.sides)

  #define classmethod 'getValue' to return the current value of the MSdie
  def getValue(self):
    return self.value

  #define classmethod 'setValue' to set the die to a particular value
  def setValue(self, value):
    self.value = value