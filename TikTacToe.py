from tkinter import *
import tkinter as tk
from typing import Dict
from functools import partial
from tkinter import messagebox

XTurn = True
OTurn = False
Xclicked = True
Oclicked = False
Winner = False

class TikTacToe:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("TikTacToe")

        self.TitleLabel = tk.Label(self.mainWin, bg="grey", text="TikTacToe")
        self.TitleLabel.config(font=('Times', 25))
        self.TitleLabel.grid(row=0, column=2)

        gameData = {}
        gameData["currentPlayer"] = "X"
        gameData["count"] = 0

        Board = self.OfficialBoard(gameData)

        # Quit and Restart Buttons

        RestartButton = tk.Button(self.mainWin, text="Restart")
        RestartButton.grid(row=0, column=3)
        RestartButton["command"] = self.restart

        QuitButton = tk.Button(self.mainWin, text="Quit")
        QuitButton.grid(row=0, column=1)
        QuitButton["command"] = self.quit

    # Button for three by three board

    def OfficialBoard(self, gameData):
        gameData["Button1"] = 0
        self.Button1 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button1", self.Button1, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button1.grid(row=1, column=1)
        if self.Button1 is True:
            gameData["Button1"] = 1
        gameData["Button2"] = 0
        self.Button2 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button2", self.Button2, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button2.grid(row=1, column=2)
        if self.Button2 is True:
            gameData["Button2"] = 1
        gameData["Button3"] = 0
        self.Button3 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button3", self.Button3, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button3.grid(row=1, column=3)
        if self.Button3 is True:
            gameData["Button3"] = 1
        gameData["Button4"] = 0
        self.Button4 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button4", self.Button4, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button4.grid(row=2, column=1)
        if self.Button4 is True:
            gameData["Button4"] = 1
        gameData["Button5"] = 0
        self.Button5 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button5", self.Button5, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button5.grid(row=2, column=2)
        if self.Button5 is True:
            gameData["Button5"] = 1
        gameData["Button6"] = 0
        self.Button6 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button6", self.Button6, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button6.grid(row=2, column=3)
        if self.Button6 is True:
            gameData["Button6"] = 1
        gameData["Button7"] = 0
        self.Button7 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button7", self.Button7, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button7.grid(row=3, column=1)
        if self.Button7 is True:
            gameData["Button7"] = 1
        gameData["Button8"] = 0
        self.Button8 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button8", self.Button8, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button8.grid(row=3, column=2)
        if self.Button8 is True:
            gameData["Button8"] = 1
        gameData["Button9"] = 0
        self.Button9 = tk.Button(self.mainWin, height=5, width=15, bg='grey', relief=tk.RAISED, font=('Times', 15),
                                 command=partial((lambda: (makeMove("Button9", self.Button9, gameData), self.checkwin(gameData), self.IfTie(gameData)))))
        self.Button9.grid(row=3, column=3)
        if self.Button9 is True:
            gameData["Button9"] = 1
        return (self.Button1, self.Button2, self.Button3, self.Button4, self.Button4, self.Button4, self.Button5,
                self.Button6, self.Button7, self.Button8, self.Button9)

    def IfTie(self, gameData):
        if gameData["count"] == 9 and Winner == False:
            msg_box = messagebox.askquestion("Tie", "The Game Was a Tie! Would you like to play again")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()

    def checkwin(self, gameData):
        global Winner
        if gameData["Button1"] == 1 and gameData["Button2"] == 1 and gameData["Button3"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button1"] == 2 and gameData["Button2"] == 2 and gameData["Button3"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button4"] == 1 and gameData["Button5"] == 1 and gameData["Button6"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button4"] == 2 and gameData["Button5"] == 2 and gameData["Button6"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button7"] == 1 and gameData["Button8"] == 1 and gameData["Button9"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button7"] == 2 and gameData["Button8"] == 2 and gameData["Button9"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button1"] == 1 and gameData["Button4"] == 1 and gameData["Button7"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button1"] == 2 and gameData["Button4"] == 2 and gameData["Button7"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button2"] == 1 and gameData["Button5"] == 1 and gameData["Button8"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button2"] == 2 and gameData["Button5"] == 2 and gameData["Button8"] == 2:
            Winner = True
            print("O Wins")
        if gameData["Button3"] == 1 and gameData["Button6"] == 1 and gameData["Button9"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button3"] == 2 and gameData["Button6"] == 2 and gameData["Button9"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button1"] == 1 and gameData["Button5"] == 1 and gameData["Button9"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button1"] == 2 and gameData["Button5"] == 2 and gameData["Button9"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button3"] == 1 and gameData["Button5"] == 1 and gameData["Button7"] == 1:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "X Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()
        if gameData["Button3"] == 2 and gameData["Button5"] == 2 and gameData["Button7"] == 2:
            Winner = True
            msg_box = messagebox.askquestion("Winner", "O Wins! Do you want to play again?")
            if msg_box == 'yes':
                self.restart()
            if msg_box == "no":
                self.quit()

    def run(self):
        """This takes no inputs, and sets the GUI running"""
        self.mainWin.mainloop()

    def quit(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.mainWin.destroy()

    def restart(self):
        """Destroys the current game, and creates a new checkers game"""
        self.mainWin.destroy()
        myTikTacToe = TikTacToe()
        myTikTacToe.run()


def makeMove(dict, B, gameData):
    global Xclicked, Oclicked
    if B["text"] == "" and Xclicked is True:
        B["text"] = "X"
        Xclicked = False
        Oclicked = True
        gameData["count"] = gameData["count"] + 1
        gameData.update({dict: 1})
        print(gameData)
    elif B["text"] == "" and Oclicked is True:
        B["text"] = "O"
        Xclicked = True
        Oclicked = False
        gameData["count"] = gameData["count"] + 1
        gameData.update({dict: 2})
        print(gameData)
    else:
        messagebox.showerror("TikTacToe", "Square is full!")

tik = TikTacToe()
tik.run()
