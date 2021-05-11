import d20
import tkinter as tk

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
    print("What are you rolling for?")
    global dndType
    dndType = input("Attack, Skill Check, Saving Throw,") # this is unfineshed btw

def dndStats(): # This should only happen once, or when character is reset. perhaps we could save multiple characters. Nonetheless this should be replaced by the tkinter interface instead of a prompt. With the interface we could save different profiles
    dndCharLvl = input("What is your Characters Level? ")
    dndCharStr = input("What is your [Strength] Ability Score? ")
    dndCharDex = input("What is your [Dexterity] Ability Score? ")
    dndCharCon = input("What is your [Constitution] Ability Score? ")
    dndCharInt = input("What is your [Intelligence] Ability Score? ")
    dndCharWis = input("What is your [Wisdom] Ability Score? ")
    dndCharCha = input("What is your [Charisma] Ability Score? ")
    
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
        dndCharRoll = d20.roll("4d6kh3")
        str(dndCharRoll)
        print(dndCharRoll)

    
def dndHelp():
    print("Inputs are formatted Dice-Count 'd' Dice-Type '+' Modifier")
    print("Suggested dice for this system: d4, d6, d8, d10, d12, d20, d100.")
    print("Example: 1d20+2 ")
    print('To Go back type "Back"')


def wh40kStart():
'''
def wh40kDiceCalc():

def wh40kDiceInput():
'''

Start()

# TKINTER TIME :)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        