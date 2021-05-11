from tkinter import *
import d20
import random
import sys

root = Tk()

# Dice Variables
logoImage = (PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo1.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo2.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo3.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo4.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo5.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\Icons\DiceLogo6.png"),)
diceImage = (PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice1.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice2.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice3.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice4.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice5.png"), PhotoImage(file = r"C:\Users\tavss\Documents\GitHub\Dice-Calculator\dice6.png"))
diceTypeName = ("d4", "d6", "d8", "d10", "d12", "d20")
# Sytem Variables
systemName = ("Dungeons & Dragons", "Warhammer 40.000")
systemColor = ('#ed2228', '#446276')
# Other Variables
randomLogo = random.randint(1,6)

class Application(Frame):  # Application is a Frame (inheritance from Frame)
    def __init__(self, master):
        Frame.__init__(self, master) 
        self.grid(sticky=N+S+E+W) # put frame in toplevel window
        self.createWidgets()

    def commandHandler(self, bNo):
        print("Cmd handler called: " + str(bNo))

    def createWidgets(self):
        top=self.winfo_toplevel()
        #top.geometry("500x500")
        top.rowconfigure(0, weight=1)     # toplevel window rows scalable
        top.columnconfigure(0, weight=1)  # toplevel window colums scalable
        
        # rows with minimum size and equal weights
        for row in range(0,10):
            self.rowconfigure(row, weight=1 , minsize=200)

        # columns with different scale
        for i in range(0,10):
            self.columnconfigure(i, weight=i, minsize=400)
        
        # Buttons and Text
        systemIndicator = Button(text=systemName[0], bg=systemColor[0])
        systemIndicator.grid(column=0, row=0, columnspan=8, sticky = N+W+E+S)

        diceCountLabel = Label(text="Dice Count", compound=LEFT)
        diceCountLabel.grid(column=0, row=1, columnspan=2, sticky = N+W+E+S)

        diceCountEntry = Entry()
        diceCountEntry.grid(column=1, row=1, columnspan=2, sticky = N+W+E+S)

        rollButton = Button(text="ROLL!", bg='#8e478c')
        rollButton.grid(column=0, row=3, columnspan=2, rowspan=2, sticky = N+W+E+S)

        advantageButton = Button(text="Advantage", bg='#71aa34')
        advantageButton.grid(column=2, row=3, columnspan=3, rowspan=2, sticky = N+W+E+S)

        disadvantageButton = Button(text="Disadvantage", bg='#a93b3b')
        disadvantageButton.grid(column=5, row=3, columnspan=3, rowspan=2, sticky = N+W+E+S)



        for i1 in range(0,6):
            diceTypeButton = Button(text=diceTypeName[i1], image = diceImage[i1], compound=RIGHT)
            diceTypeButton.grid(column=i1+2, row=1, rowspan=2, sticky = N+W+E+S)

        

app = Application(root)
app.master.title("Dice Calculator")
app.master.wm_iconphoto(True, logoImage[randomLogo])
app.mainloop()
