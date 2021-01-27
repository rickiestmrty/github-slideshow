from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time

root = Tk()
root.title("TicTacToe Game")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight-150,positionDown-150))

class TicTacToe:
    player = "Player 1"
    textC = "X"
    turn_lbl = Label(root, text=player+"'s turn ("+textC+")",font=("Courier",25))
    turn_lbl.grid(columnspan=3, row=0, ipadx = 25, ipady = 25)

    def __init__(self,checkAi=False):
        self.checkAi=checkAi
        self.button=[]
        self.row=1
        self.column=0
        self.player = "Player 1"
        self.textC = "X"
        self.turn_lbl.config(text=self.player+"'s turn ("+self.textC+")")
        
    def checkWinner(self): 
        unusedBtns=9

        if (self.button[0]['text']==self.textC and self.button[1]['text']==self.textC and self.button[2]['text']==self.textC or
        self.button[3]['text']==self.textC and self.button[4]['text']==self.textC and self.button[5]['text']==self.textC or
        self.button[6]['text']==self.textC and self.button[7]['text']==self.textC and self.button[8]['text']==self.textC or
        self.button[0]['text']==self.textC and self.button[4]['text']==self.textC and self.button[8]['text']==self.textC or
        self.button[6]['text']==self.textC and self.button[4]['text']==self.textC and self.button[2]['text']==self.textC or
        self.button[0]['text']==self.textC and self.button[3]['text']==self.textC and self.button[6]['text']==self.textC or
        self.button[1]['text']==self.textC and self.button[4]['text']==self.textC and self.button[7]['text']==self.textC or
        self.button[2]['text']==self.textC and self.button[5]['text']==self.textC and self.button[8]['text']==self.textC):
            messagebox._show("Winner",self.player+" wins the game!")
            return True
        else:
            for i in range(0,9):
                if self.button[i]['text'] != " ":
                    self.button[i]["state"]="disabled"
                    unusedBtns-=1
            if unusedBtns == 0:
                messagebox._show("Draw","The game ends in a draw!")
                return True
            return False
    
    def computerMove(self):
        available_btn=[]
        j=0
        for i in range(0,9):
            if self.button[i]['text']==" ":
                available_btn.append(i)
                j+=1
        index = random.choice(available_btn)
        self.buttonPressed(index)

    def buttonPressed(self,index):
        self.button[index].config(text=self.textC)
        if self.checkWinner() == False:
            if self.checkAi==False:
                if self.textC == "X":
                    self.textC = "O"
                    self.player = "Player 2"
                else:
                    self.textC = "X"
                    self.player = "Player 1"
                self.turn_lbl.config(text=self.player+"'s turn ("+self.textC+")")
            else:
                if self.textC == "X":
                    self.textC = "O"
                    self.player = "AI"
                    self.computerMove()
                else:
                    self.textC = "X"
                    self.player = "Player 1"
                self.turn_lbl.config(text="Your turn ("+self.textC+")")
                
        else:
            root.destroy()
    
    def buttonCreation2(self,index):
        self.button.append(ttk.Button(root, text=" ", command = lambda:self.buttonPressed(index)))
        self.button[index].grid(row=self.row, column=self.column, ipadx=50, ipady=50)

    def buttonCreation(self):
        self.row+=1
        for i in range(0,9):
            self.buttonCreation2(i)
            self.column+=1
            if self.column == 3:
                self.column=0
                self.row+=1

    def startGame(self):
        self.buttonCreation()

def versusPlayer2():
    TicTacToe().startGame()

def versusAI():
    TicTacToe(True).startGame()

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu,tearoff=0)
var = IntVar()
var.set(0)
menu.add_cascade(label="Opponent",menu=subMenu)
subMenu.add_radiobutton(label="Vs Player 2",variable=var,value=0,command = lambda:versusPlayer2())
subMenu.add_radiobutton(label="Vs AI",variable=var,value=1,command = lambda:versusAI())

versusPlayer2()

root.mainloop()