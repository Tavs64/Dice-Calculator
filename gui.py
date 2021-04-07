from tkinter import *
import sys

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
        for row in range(0,7):
            self.rowconfigure(row, weight=1 , minsize=100)

        # columns with different scale
        for i in range(0,7):
            self.columnconfigure(i, weight=i, minsize=200)
        
        # Buttons
        



root = Tk()

app = Application(root)
app.master.title("Min applikation")
app.mainloop()
