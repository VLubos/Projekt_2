"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Luboš Vavruška
email: lubos.vavruska@seznam.cz
discord:
"""

import random

def BullsAndCows():
    separator = 20*"-"
    print(f"""Hi there!\n
{separator}\n
I've generated a random 4 digit number for you.\n
Let's play a bulls and cows game.\n
{separator}\n""")
   
    def digitSelection(rangeLow: int, rangeHigh: int) -> int:
        digit = random.choice(range(rangeLow, rangeHigh))
        return digit

    def numberGeneration() -> list:
        number = [0, 0, 0, 0]
        number[0] = digitSelection(1, 10)
        number[1] = digitSelection(0, 10)
        number[2] = digitSelection(0, 10)
        number[3] = digitSelection(0, 10)
        return number
    
    def defineNumber():
        guess = input(f"Enter a number:\n{separator}\n>>> ")
        guessList = list(guess)
        return guessList       

    def compareInput(guessed: list, given: list) -> list:
        direct = 0
        indirect = 0
        for indexGuessed, memberGuessed in enumerate(guessed):
            for indexGiven, memberGiven in enumerate(given):
                if int(memberGuessed) == memberGiven and indexGuessed == indexGiven:
                    direct += 1
                elif int(memberGuessed) == memberGiven and indexGuessed != indexGiven:
                    indirect += 1
        return [direct, indirect]

        
    comparator = numberGeneration()
    tries = 0
    gameOn = True

    while gameOn:
        result = compareInput(defineNumber(), comparator)
        tries += 1
        bulls = result[0]
        cows = result[1]
        if bulls != 4:
            if bulls == 1:
                bullstring = "1 bull"
            elif bulls == 0 or bulls == 2 or bulls == 3:
                bullstring = (f"{bulls} bulls")
            if cows == 1:
                cowstring = "1 cow"
            elif cows == 0 or cows == 2 or cows == 3: 
                cowstring = (f"{cows} cows")
            print(f"{bullstring}, {cowstring}")
        elif bulls == 4:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            if tries < 5:
                print("That is amazing!")
            elif tries >= 5 and tries < 10:
                print("That is average")
            else:
                print("Not so good")
            gameOn == False
            break
        
if __name__ == "__main__":
    BullsAndCows()
    
        
        
                          

