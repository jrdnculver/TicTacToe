import tkinter as tk

'''
Jordan Culver
SDEV 220
Tic Tac Toe Game
Due March 16, 2022
'''


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x600")
        self.window.title("Tic Tac Toe Game")
        self.boardTracker = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.count = 0
        self.update = tk.StringVar()
        self.winner = None
        self.playing = True
        self.placeNumbers = ["one", "two", "three",
                             "four", "five", "six", "seven", "eight", "nine"]
        self.markerPlacement = [[228, 130], [352, 130], [476, 130], [228, 250], [
            352, 250], [476, 250], [228, 370], [352, 370], [476, 370]]
        self.matrixIndex = [[0, 0], [0, 1], [0, 2], [
            1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.touchEquivalence = [x for x in range(1, 10)]

    def run(self):
        self.canvas = tk.Canvas(self.window, width=700, height=600, bg="white")
        for x in self.touchEquivalence:
            self.canvas.bind(x, self.playedSelection)
        self.canvas.bind('<space>', self.newGame)
        self.canvas.pack()
        self.board = tk.PhotoImage(file="Images/tictactoeBoard.png")
        self.xPiece = tk.PhotoImage(file="Images/x.png")
        self.oPiece = tk.PhotoImage(file="Images/o.png")
        self.numPictures = [self.one, self.two, self.three, self.four, self.five,
                            self.six, self.seven, self.eight, self.nine] = self.initalizeNumbers()
        self.x = 350
        self.y = 250
        self.canvas.create_image(
            self.x, self.y, image=self.board, tags="board")
        self.canvas.focus_set()
        self.labels()
        self.updateLabel()
        self.gridNumbers()
        self.updateText("Player One Turn")

        self.window.mainloop()

    def initalizeNumbers(self):
        pictures = []
        i = 0
        for values in self.placeNumbers:
            pic = tk.PhotoImage(file="Images/" + f"{self.placeNumbers[i]}.png")
            pictures.append(pic)
            i += 1

        return pictures

    def gridNumbers(self):
        i = 0
        for pic in self.numPictures:
            numValues = self.markerPlacement[i]
            x, y = numValues
            self.canvas.create_image(
                x, y, image=self.numPictures[i])
            i += 1

    def updateLabel(self):
        win = tk.Label(self.canvas, fg="blue",
                       textvariable=self.update, font=(512))
        win.place(relx=.5, rely=.8, anchor="center")

    def updateText(self, updatedText):
        self.update.set(value=updatedText)

    def labels(self):
        header = tk.Label(self.canvas, fg="black",
                          text="Tic Tac Toe", font=(256))
        header.place(relx=.5, rely=.05, anchor="center")

        newGame = tk.Label(self.canvas, fg="blue",
                           text="SpaceBar for New Game", font=(256))
        newGame.place(relx=.85, rely=.95, anchor="center")

    def playedSelection(self, event):
        for number in self.touchEquivalence:
            if (event.char == f"{number}"):
                bt1, bt2 = self.matrixIndex[number-1]
                x, y = self.markerPlacement[number-1]
                break

        self.playerTurn(x, y, bt1, bt2)

    def playerTurn(self, x, y, bt1, bt2):
        if self.boardTracker[bt1][bt2] == 0 and self.playing == True:
            if self.turn == 1:
                self.canvas.create_image(
                    x, y, image=self.xPiece)
                self.changeTurn()
                self.boardTracker[bt1][bt2] = 1
                self.updateText("Player Two Turn")
            else:
                self.canvas.create_image(
                    x, y, image=self.oPiece)
                self.changeTurn()
                self.boardTracker[bt1][bt2] = 2
                self.updateText("Player One Turn")
        self.winner = self.winners("Player One", 1)
        if self.winner == None:
            self.winner = self.winners("Player Two", 2)
        if self.winner != None:
            self.playing = False
            self.updateText(self.winner)

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
            self.count += 1
        else:
            self.turn = 1
            self.count += 1

    def winners(self, playerName, num):
        self.winValues = [[[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [
            [0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]

        win = []
        number = 0

        for values in range(0, 3):
            if self.boardTracker[values] == [num, num, num]:
                return f"{playerName} Wins"

        while number < 5:
            for values in self.winValues[number]:
                x, y = values
                if self.boardTracker[x][y] == num:
                    win.append("X")
                    if len(win) == 3:
                        return f"{playerName} Wins"
            number += 1
            win.clear()

        for values in range(0, 3):
            if 0 not in self.boardTracker[values]:
                win.append("X")
                if len(win) == 3:
                    return "Player Draw"

        win.clear()

    def newGame(self, event):
        self.window.destroy()
        tic = TicTacToe()
        tic.run()


if __name__ == "__main__":
    tic = TicTacToe()
    tic.run()
