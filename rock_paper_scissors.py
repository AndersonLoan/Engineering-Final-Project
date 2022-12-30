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

from random import randint

database = ['rock', "paper", "scissors"]
count = 1 
humanscore = 0 
computerscore = 0
userguesses = []
response = ["y","n","yes","no"]

def comparison(human,computer):
    """
    checks the user input and computer input and returns the fictor

    Parameters
    ----------
    human : string
        is the user choice between rock paper and scisssors.
    computer : string
        is the computers choice between rock paper and scissors.

    Returns
    -------
    returns the comparison between the user and the computer

    """
    global humanscore
    global computerscore
    if human == 'rock' and computer == 'scissors':
        humanscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Player won!")
        print("SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Player needs {5 - humanscore} to win")
    elif human == 'rock' and computer == 'paper':
        computerscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Computer won!")
        print("SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Computer needs {5 - computerscore} to win")
    elif human == 'paper' and computer == 'rock':
        humanscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Player won!")
        print(f"SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Player needs {5 - humanscore} to win")
    elif human == 'paper' and computer == 'scissors':
        computerscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Computer won!")
        print("SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Computer needs {5 - computerscore} to win")
    elif human == 'scissors' and computer == 'paper':
        humanscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Player won!")
        print("SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Player needs {5 - humanscore} to win")
    elif human == 'scissors' and computer == 'rock':
        computerscore += 1
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("Computer won!")
        print(f"SCORE BOARD".center(30) + f"\nHuman Score:{humanscore}\tComputer Score:{computerscore}")
        print(f"Computer needs {5 - computerscore} to win")
    else:
        print(f"Player choose:{human}\tComputer choose:{computer}")
        print("DRAW!")
        print('No point is given')
def computerguess(n):
    """
    creates the computer input of rock paper scissors

    Parameters
    ----------
    n : integer
        is used to pick a choice out of a list that contains rock paper and scissors

    Returns an index of a list of rock paper scissors based on the random number from 0-2
    -------
    None.

    """
    computer_guess = ["rock","scissors","paper"]
    return(computer_guess[n])


def game():
    global count
    print("Hello!")
    print("You have choosen to play Rock Paper Scissors")
    print("You and the computer will compete until one of you reaches 5 won rounds")
    print("You will choose either Rock Paper or Scissors...")
    print("I know complicated")
    print("The computer will then make it's choice")
    print("Whoever wins the round is awarded a point")
    print("")
    while True:
    
        user = input("Are you ready to play?(Y/N)").lower()
        if user in response and user == 'y' or user == "yes":
            print("______________________________________________")
            print("")
            print("ROUND 1")
            print("______________________________________________")
            
            user = input("Rock Paper Scissors: ").lower()
            while True:
                try:
                    if database[database.index(user)]:
                        ai = randint(0,2)
                        comparison(user,computerguess(ai))
                        count += 1
                    if humanscore == 5 or computerscore == 5:
                        break
                    else:
                        print("______________________________________________")
                        print("")
                        print(f"ROUND {count}")
                        print("______________________________________________")
                        user = input("Rock Paper Scissors: ").lower()
                    
                except:
                    user = input("Wrong Input try again: ").lower()
                    continue
            print("______________________________________________")
            print("\n")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            if humanscore > computerscore:
                print('@  Congratulations Human, you have bested machine!  @')
            else:
                print("@ " + "    The Machine won, who would've guessed" +  "         @")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            
            
        
        elif user in response and user == "n" or user == "no":
            user = input("Do you wish to return to main menu?(Y/N)").lower()
            if user in response and user == "n" or user == "no":
                continue
            elif user in response and user == "y" or user == "yes":
                break
            else:
                print("")
                user = input("ERROR: Not a valid response")
                continue
        else:
            print("")
            print("ERROR: Not a valid response")
            continue
            
        
        
    
    
