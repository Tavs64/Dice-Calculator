import math                                                    #   The math library will allow us to make more complex equations
import tkinter                                                 #   The Tkinter library will allow us to make a GUI for our program
import random                                                  #   The Random library will allow us to generate random numbers

def diceRoll(x,y,z):                                           #   x = Dice Count, y = Dice Type or Max Value, z = Minimum roll to succeed
    global total                                               #   The total value will be used throughought different functions, and making it global will make it a smoother process
    total = 0                                                  #   Resets the total value before every roll
    while (x != 0):                                            #   Loop that ensures that only the specified amount of dice are rolled
        roll = random.randint(1,y)                             #   Generates a random number between 0 and the specified Max Value
        if (roll <= z):                                        #   If the roll is beneath the Minimum roll to succeed
            str(roll)                                          #   Turns the roll into a string so it behaves nicely as with print
            print("\033[1m" + roll,'Failed' + "\033[0m")       #   Outputs that roll has failed, the "\033[1m" and "\033[0m" make whatever is between them bold
            x = x+1                                            #   One is added to the loop, so this roll isnt lost.
        if (roll > z):                                         #   If the roll is above the Minimum roll to succeed
            print(roll)                                        #   Outputs the roll as is
            total = roll + total                               #   The roll is added to the totall
        x = x-1        