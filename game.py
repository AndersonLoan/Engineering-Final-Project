# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: YOUR NAME
# Section: YOUR SECTION NUMBER
# Assignment: THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date: DAY MONTH YEAR
#

#
# YOUR CODE HERE
#

from rock_paper_scissors import game
from blackjack import blackjack
from War import war

print("Hello, welcome to Anderson and Andrew's game collection!")
print("What Game would you like to play?")
while True:
    print()
    print("If you're done playing type 'EXIT'")
    print("Enter 1, 2, or 3: ")
    print("1.Rock Paper Scissors\n2.Black Jack\n3.War")
    user = input("").upper()
    if user == '1':
        game()
    elif user == '2':
        blackjack()
    elif user == '3':
        war()
    elif user == "EXIT":
        break
        
        