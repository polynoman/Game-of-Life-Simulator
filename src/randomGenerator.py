'''

    randomGenerator

 This class is used to generate random initial states for the Game of Life.
 A custom seed can be specified to generate a specific initial state.

 '''

import random


class randomGenerator:

    def __init__(self, seed=None, threshold=0.35, fieldX=50,  fieldY=50):
        self.seed = seed
        self.threshold = threshold
        self.fieldX = fieldX
        self.fieldY = fieldY

        if seed != None:
            random.seed(self.seed)


    def generateMatrix(self):
        matrix = list()
        for ii in range(self.fieldY):
            a = list()
            for i in range(self.fieldX):
                a.append(0)
            matrix.append(a)

        for i in range(0,len(matrix)):
            for ii in range(0,len(matrix[i])):
                if random.random() < self.threshold:
                    matrix[i][ii] = 1
                else:
                    matrix[i][ii] = 0

        return matrix


if __name__ == "__main__":
    rg = randomGenerator()
    print(rg.generateMatrix())
