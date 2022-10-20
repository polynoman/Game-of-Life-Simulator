'''

    randomGenerator

 This class is used to generate random initial states for the Game of Life.
 A custom seed can be specified to generate a specific initial state.

 '''

import random


class randomGenerator:

    def __init__(self, seed=None, threshold=0.35, fieldX=50, fieldY=50):
        self.seed = seed
        self.threshold = threshold
        self.fieldX = fieldX
        self.fieldY = fieldY

        if seed != None:
            random.seed(self.seed)


    def generateMatrix(self):
        matrix = []
        for _ in range(self.fieldY):
            a = [0 for _ in range(self.fieldX)]
            matrix.append(a)

        for item in matrix:
            for ii in range(len(item)):
                item[ii] = 1 if random.random() < self.threshold else 0
        return matrix


if __name__ == "__main__":
    rg = randomGenerator()
    print(rg.generateMatrix())
