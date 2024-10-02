#Author: Phuong Tran
#Date: 09/30/2024
#Description: 

from die import Die

class Player:
    """ Represent a list of 3 Die objects and the player's point
        Attributes:
            _dice (list): list of 3 Die objects
            _point (int): player's points
        Methods:
            __init__(self): constructa and sorts the list of 3 Die objects and the Player's point (default = 0)
            get_points(self): return the player's points
            roll_dice(self): calls roll on each of the Die objects in the dice list and sorts the list.
            has_pair(self): returns true if two dice in the list have the same value (uses ==). Increments points by 1.
            has_three_of_a_kind(self): returns true if all three dice in the list have the same value (uses ==). Increments points by 3.
            has_series(self): returns true if the values of each of the dice in the list are in a sequence (ex. 1,2,3 or 2,3,4 or 3,4,5 or 4,5,6) (uses -). Increments points by 2.
            __str__(self): returns a string in the format: “D1=2, D2=4, D3=6”
    """
    def __init__(self):
        self._dice = [Die(), Die(), Die()]
        self._dice.sort()
        self._point = 0

    def get_points(self):
        return self._point
    
    def roll_dice(self):
        #for each die object in the list, call the roll method to roll the die
        for die in self._dice:
            die.roll()
        self._dice.sort()

    def has_pair(self): #+1
        for i in range(len(self._dice)):
            for j in range(i+1,len(self._dice)):
                if self._dice[i] == self._dice[j]:
                    self._point +=1
                    return True
        return False

    def has_three_of_a_kind(self): #+3
        if self._dice[0] == self._dice[1] == self._dice[2]:
            self._point += 3
            return True
        return False

    def has_series(self): #+2
        if (self._dice[1] - self._dice[0] == 1) and (self._dice[2] - self._dice[1] == 1):
            self._point += 2
            return True
        return False

    def __str__(self):
        s = ""
        for index, die in enumerate(self._dice):
            s += "D" + str(index+1) + "= " + str(die) + " " 
        return s
