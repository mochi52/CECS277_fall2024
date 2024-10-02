Yahtzee

A dice game that awards the user points for a pair, three-of-a-kind, or a series.
***
Die class (die.py) – has two attributes: the number of sides of the die and the value of the rolled
die.
      1. __init__(self, sides=6) – assigns the number of sides from the value passed in. Set
      value to 0 or to the returned value of roll().
      2. roll(self) – generate a random number between 1 and the number of sides and assign
      it to the Die’s value. Return the value.
      3. __str__(self) – return the Die’s value as a string.
      4. __lt__(self, other) – return whether the value of self is less than the value of other.
      5. __eq__(self, other) – return whether the value of self is equal to the value of other.
      6. __sub__(self, other) – return the difference between the value of self and the value
      of other.
***
Player class (player.py) – has two attributes: a list of 3 Die objects and the player’s points.
      1. __init__(self) – constructs and sorts the list of three Die objects and initializes the
      player’s points to 0.
      2. get_points(self) – returns the player’s points.
      3. roll_dice(self) – calls roll on each of the Die objects in the dice list and sorts the list.
      4. has_pair(self) – returns true if two dice in the list have the same value (uses ==).
      Increments points by 1.
      5. has_three_of_a_kind(self) – returns true if all three dice in the list have the same
      value (uses ==). Increments points by 3.
      6. has_series(self) – returns true if the values of each of the dice in the list are in a
      sequence (ex. 1,2,3 or 2,3,4 or 3,4,5 or 4,5,6) (uses -). Increments points by 2.
      7. __str__(self) – returns a string in the format: “D1=2, D2=4, D3=6”.
***
Main file (main.py) – has one function named take_turn that passes in a Player object. The
take_turn function should: roll the player’s dice, display the dice, check for and display any win
types (pair, series, three-of-a-kind), and display the updated score. The main function should
construct a player object, and then repeatedly call take_turn until the user chooses to end the
game. Display the final points at the end of the game. Use the check_input module’s
get_yes_no function to prompt the user to continue or end the game. Use docstrings to document
each class, method, and function.



Example Output (user input in italics):
-Yahtzee-
D1=1 D2=4 D3=5
Aww. Too Bad.
Score = 0
Play again? (Y/N):
g
Invalid input - should be a 'Yes'
or 'No'.
Play again? (Y/N):
y
D1=3 D2=3 D3=5
You got a pair!
Score = 1
Play again? (Y/N):
y
D1=3 D2=4 D3=5
You got a series of 3!
Score = 3
Play again? (Y/N):
y
D1=1 D2=1 D3=1
You got 3 of a kind!
Score = 6
Play again? (Y/N):
n
Game Over.
Final Score = 6
