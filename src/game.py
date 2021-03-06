#=============================================================================#
#                      Conway's Game of Life Version 1.0                      #
#=============================================================================#


import os
import time
import copy
import examples
import gui, randomGenerator

class gameOfLife:

    def __init__(self, matrix, intervall=0.75, trace=False, gui=True):
        self.elementCharacter = "o"
        self.voidCharacter = "-"
        self.lineBreakCharacter = "\n"

        self.gameMatrix = matrix
        self.intervall = intervall
        self.trace = trace
        self.gui = gui

        if gui:
            self.setupGui()
        else:
            self.doMultipleSteps(-1)


    def printMatrix(self, space = 0):
        output = ""
        for i in range(len(self.gameMatrix)):
            for ii in range(len(self.gameMatrix[i])):
                if self.gameMatrix[i][ii]:
                    output += " " + self.elementCharacter
                else:
                    output += " " + self.voidCharacter
            output += self.lineBreakCharacter
        for i in range(space):
            output += ("\n")
        print(output)


    def doStep(self):
        matrixCopy = copy.deepcopy(self.gameMatrix)
        for i in range(0,len(self.gameMatrix)):
            for ii in range(0,len(self.gameMatrix[i])):
                neighbors = 0
                for xoffset in range(-1,2):
                    for yoffset in range(-1,2):
                        xCord = i + xoffset
                        if xCord >= len(self.gameMatrix):
                            xCord = 0
                        elif xCord < 0:
                            xCord = len(self.gameMatrix)-1
                        yCord = ii + yoffset
                        if yCord >= len(self.gameMatrix[i]):
                            yCord = 0
                        elif yCord < 0:
                            yCord = len(self.gameMatrix[i])-1
                        if self.gameMatrix[xCord][yCord]:
                            neighbors += 1
                if self.gameMatrix[i][ii] == 1:
                    neighbors -= 1
                    if neighbors < 2 or neighbors > 3:
                        matrixCopy[i][ii] = 0
                elif self.gameMatrix[i][ii] == 0:
                    if neighbors == 3:
                        matrixCopy[i][ii] = 1
        self.gameMatrix = matrixCopy


    def doMultipleSteps(self, stepAmount):
        i=0
        while (i+1) != stepAmount:
            self.doStep()
            self.printMatrix()
            i+=1
            time.sleep(self.intervall)


    def setupGui(self):
        app = gui.App(game=self)
        app.mainloop()



if __name__ == "__main__":

    rg = randomGenerator.randomGenerator(seed="hallo123123", fieldY=24)
    gameMatrix = rg.generateMatrix()

    game = gameOfLife(gameMatrix)
