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
   
    def duplicateCheck(checkedNumber: list) -> bool:
        randomNumber = False
        for i in range (0, 4):
            if checkedNumber.count(checkedNumber[i]) > 1:
                randomNumber = False
                break
            elif checkedNumber.count(checkedNumber[i]) == 1:
                randomNumber = True
        return randomNumber

    def digitSelection() -> list:
        numberOK = False
        while numberOK is False:
            FourDigits = str(random.choice(range(1000, 9999)))
            FourDigitsToList = list(FourDigits) 
            numberOK = duplicateCheck(FourDigitsToList)
        return FourDigitsToList
    
    def defineNumber() -> list:
        numberIncorrect = True
        while numberIncorrect:
            guess = input(f"Enter a number:\n{separator}\n>>> ")
            guessList = list(guess)
            if guessList[0] == "0" or len(guessList) != 4  or duplicateCheck(guessList) is False or guess.isnumeric() is False:
                numberIncorrect
                print("Incorrect entry, please try again")
            else:
                numberIncorrect = False
        return guessList       

    def compareInput(guessed: list, given: list) -> list:
        direct = 0
        indirect = 0
        for indexGuessed, memberGuessed in enumerate(guessed):
            for indexGiven, memberGiven in enumerate(given):
                if int(memberGuessed) == int(memberGiven) and indexGuessed == indexGiven:
                    direct += 1
                elif int(memberGuessed) == int(memberGiven) and indexGuessed != indexGiven:
                    indirect += 1
        return [direct, indirect]

    def stringMaker(count: int, word: str) -> str:
        if count == 1:
            countString = (f"1 {word}")
        elif count == 0 or count == 2 or count == 3:
            countString = (f"{count} {word}s")
        return countString

        
    comparator = digitSelection()
    tries = 0
    gameOn = True
    while gameOn:
        cislo = defineNumber()
        result = compareInput(cislo, comparator)
        tries += 1
        bulls = result[0]
        cows = result[1]
        if bulls != 4:
            a = stringMaker(bulls, "bull")
            b = stringMaker(cows, "cow")
            print(f"{a}, {b}")
        elif bulls == 4:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            if tries < 5:
                print("That is amazing!")
            elif tries >= 5 and tries < 10:
                print("That is average")
            else:
                print("Not so good")
            gameOn is False
            break
        
if __name__ == "__main__":
    BullsAndCows()
    
        
        
                          

