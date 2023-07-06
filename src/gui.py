import tkinter as tk
from tkinter import messagebox
import random
import game, examples, game, randomGenerator

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self.title("Game of Life Simulator")

        self.cellwidth = 15
        self.cellheight = 15

        self.game = kwargs["game"]
        self.matrix = self.game.gameMatrix
        self.rows = len(self.game.gameMatrix)
        self.columns = len(self.game.gameMatrix[0])
        self.intervall = int(self.game.intervall * 1000)
        self.trace = self.game.trace

        self.canvas = tk.Canvas(self, width=self.cellwidth * self.columns, height=self.cellheight * self.rows, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand="true")

        frame = tk.Frame()

        self.grid = {}
        self.rect = {}
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.grid[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="lightgray", tags="grid", outline='lightgray')
                self.rect[row,column] = self.canvas.create_rectangle(x1+2,y1+2,x2-2,y2-2, fill="white", tags="rect", outline='white')

        if self.trace:
            self.traceDraw(self.intervall)
        else:
            self.redraw(self.intervall)


    def redraw(self, delay):
        for i in range(len(self.matrix)):
            for ii in range(len(self.matrix[i])):
                item_id = self.rect[i,ii]
                if self.matrix[i][ii] == 1:
                    self.canvas.itemconfig(item_id, fill="#22282A", outline='#22282A')
                else:
                    self.canvas.itemconfig(item_id, fill="white", outline='white')
        if (self.game.current_step != self.game.max_steps):
            self.game.doStep()
            self.matrix = self.game.gameMatrix
            self.after(delay, lambda: self.redraw(delay))
            self.game.current_step+=1
        else:
            self.openStepsFinishedPopup()


    def traceDraw(self, delay):
        for i in range(len(self.matrix)):
            for ii in range(len(self.matrix[i])):
                item_id = self.rect[i,ii]
                if self.matrix[i][ii] == 1:
                    if self.canvas.itemcget(item_id, "fill") in [
                        "white",
                        "#9a280a",
                    ]:
                        self.canvas.itemconfig(item_id, fill="#167826", outline='#167826')
                    else:
                        self.canvas.itemconfig(item_id, fill="#22282A", outline='#22282A')
                elif self.canvas.itemcget(item_id, "fill") == "#22282A":
                    self.canvas.itemconfig(item_id, fill="#9a280a", outline='#9a280a')
                else:
                    self.canvas.itemconfig(item_id, fill="white", outline='white')
        self.game.doStep()
        self.matrix = self.game.gameMatrix
        self.after(delay, lambda: self.traceDraw(delay))


    def openStepsFinishedPopup(self):
        messagebox.showinfo("Information","Maximum steps has been reached")



if __name__ == "__main__":
    rg = randomGenerator.randomGenerator(seed="hallo123123")
    matrix = rg.generateMatrix()
    game = game.gameOfLife(matrix, gui=True)
