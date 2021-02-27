import d20
import tkinter

def Start():
    print("Welcome to our Dice Calculator")
    print("Are you using Dungeons & Dragons, or Warhammer 40.000")
    global systemType
    while True:
        systemType = input("Select: ").lower().strip()
        if (systemType == "dnd" or systemType == "d&d" or systemType == "dandd" or systemType == "dand" or systemType == "dungeons & dragons" or systemType == "dungeons and dragons"):
            print("You Chose: Dungeons & Dragons")
            dndStart()
            break
        elif (systemType == "warhammer" or systemType == "warhammer40k" or systemType == "wh40k" or systemType == "40k" or systemType == "warhammer40000" or systemType == "warhammer40.000"):
            print("You Chose: Warhammer 40.000")
            wh40kStart()
            break
        else:
            print("Invalid Input")
    

def dndStart():
    print("Type Help for Help on how to Format")
    dndDiceCalc()
    
def dndDiceCalc():
    global dndInput
    while True:
        dndInput = input("Dice Roll Input: ").lower().strip()
        if (dndInput == "help"):
            dndHelp()
        elif (dndInput == "back"):
            break
        else:
            try:
                dndRoll = d20.roll(dndInput)
                str(dndRoll)
                print(" ")
                print(dndRoll)
                print(" ")
            except:
                print('Syntax Error: try writing "Help"')

def dndDiceCharCalc():
    print("Rolling Character Stats")
    for n in range(6):
        print(hej)

    
def dndHelp():
    print("Inputs are formatted Dice-Count 'd' Dice-Type '+' Modifier")
    print("Example: 1d20+2 ")
    print('To Go back type "Back"')

''' 
def wh40kStart():

def wh40kDiceCalc():

def wh40kDiceInput():
'''

Start()