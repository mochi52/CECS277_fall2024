#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 09/30/2024
#Description: A dice game that awards the user points for a pair, three-of-a-kind, or a series everytime the user roll the 3 dices

import check_input
from player import Player


def main():
    def take_turn( p : Player):
        """
        roll the player dice, display the dice, check for and display any win
        types (pair, series, three-of-a-kind), and display the updated score
        """
        #roll the dice
        p.roll_dice()

        #display the dice
        print(f"\n{p}")

        #check for wins, display message, and update score
        if p.has_pair():
            if p.has_three_of_a_kind():
                print("You got three of a kind!")
            else:
                print("You got a pair!")
        elif p.has_series():
            print("You got a series!")
        else:
            print("Aww... too bad!")
            
        #display the updated score
        print(f"Score =  {p.get_points()}")

    print ("---Yahtzee---\n")
    p = Player()
    take_turn(p)

    while True:
        choice = check_input.get_yes_no("Play again? [Y] [N]: ")
        if choice is True:
            take_turn(p)
        elif choice is False:
            print("Game over! \n")
            print(f"Final score = {p.get_points()}")
            quit()
main()