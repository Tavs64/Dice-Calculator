import math                                                                                 #   The math library will allow us to make more complex equations
import tkinter                                                                              #   The Tkinter library will allow us to make a GUI for our program
import random                                                                               #   The Random library will allow us to generate random numbers

def diceRoll(x,y):                                                                          #   Function that rolls the dice. x = Dice Count, y = Dice Type or Max Value, z = Minimum roll to succeed
    global total                                                                            #   The total value will be used throughought different functions, and making it global will make it a smoother process
    total = 0                                                                               #   Resets the total value before every roll
    while (x != 0):                                                                         #   Loop that ensures that only the specified amount of dice are rolled
        roll = random.randint(1,y)                                                          #   Generates a random number between 0 and the specified Max Value                                                                            #   The roll is added to the total
        total = roll + total                                                                #   Adds the roll to the total
        x = x-1                                                                             #   Decreases the dice count so that roll works correctly

def inputGet():                                                                             #   Function That Gets the Dice Info
    global diceType                                                                         #   Declaring a variable that determines what type of die are we using
    global diceCount                                                                        #   Declaring a variable that determines how many die are we using
    diceType = int(input("What Type of Dice? "))                                            #   Takes which type of dice
    diceCount = int(input("How Many Dice? "))                                               #   Takes how many dice 

                                                                           
inputGet()                                                                                  #   Gets the Inputs
diceRoll(diceCount,diceType)                                                                #   Rolls the dice with the input gathered from inputGet

print(diceCount,'D',diceType,'Gave a Total of:',total)                                      #   Prints the Roll

