#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 09/30/2024
#Description:

import random
class Die:
    """ Represents a single Die.  Defaults to a 6-sided die.
        Attributes:
            _sides (int): number of sides on the die.
            _value (int): the value of the rolled die.
            
        Methods:
            __init__(self, sides = 6): set default value and default side of die = 6
            roll(self): roll the die and return the int value from 1 to num of sides
            str(self): cast the die's value into string
            __lt__(self, other) : return whether the value of self is less than the value of other.
            __eq__(self, other) : return whether the value of self is equal to the value of other.
            __sub__(self, other) : return the difference between the value of self and the value of other.
    """
    def __init__(self, sides = 6):
        self._sides = sides
        self._value = 0
    
    def roll(self):
        self._value = random.randint(1, self._sides)
        return self._value
    
    def __str__(self):
        return str(self._value)
    
    def __lt__(self, other):
        return self._value <= other._value
    
    def __eq__(self, other):
        return self._value == other._value
    
    def __sub__(self, other):
        return (self._value - other._value)
