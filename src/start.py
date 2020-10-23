'''

    The CLI class for the Game of Life

 This class can be used to customize the user experience of the Game of Life. The commands are specified in the CLI file under dogs.

 '''

import sys
import game, examples, randomGenerator

if __name__ == "__main__":

    dimX = 50
    dimY = 50
    matrix = None
    example = None

    seed = None
    threshold = 0.35

    intervall = 0.75

    gui = True
    trace = False

    i = 1
    args = sys.argv
    print(args)
    while i < len(args):

        if args[i] == "-d":
            try:
                i+=1
                dimX = int(args[i])
                i+=1
                dimY = int(args[i])
            except:
                print("Input dimensions not right.")

        elif args[i] == "-s":
            try:
                i+=1
                inputString = args[i]
                if len(inputString) == dimX * dimY:
                    rows = list()
                    stringIndex = 0
                    for ii in range(dimY):
                        columns = list()
                        for iii in range(dimX):
                            columns.append(inputString[stringIndex])
                        rows.append(columns)
                    matrix = rows
                else:
                    print("Dimensions do not match for input String.")
                    sys.exit()

            except:
                print("Either input dimensions or the input string is incorrect.")

        elif args[i] == "-i":
            try:
                i+=1
                intervall = float(args[i])

            except:
                print("The intervall value is incorrect.")

        elif args[i] == "-S" or args[i] == "--seed":
            try:
                i+=1
                seed = args[i]
            except:
                print("The seed value is incorrect or no seed specified.")

        elif args[i] == "-tr":
            try:
                i+=1
                threshold = float(args[i])
            except:
                print("The threshold value is incorrect or no seed specified.")

        elif args[i] == "-e":
            try:
                i+=1
                example = args[i]
            except:
                print("The example is incorrect or no example specified.")

        elif args[i] == "-cli":
            try:
                gui = False
            except:
                print("The example is incorrect or no example specified.")

        elif args[i] == "-trace":
            try:
                trace = True
            except:
                print("The example is incorrect or no example specified.")

        i+=1


    if example != None:
        if example == "blinker":
            matrix = examples.blinker
        elif example == "block":
            matrix = examples.block
        elif example == "blinker2":
            matrix = examples.blinker2
        elif example == "empty":
            matrix = examples.empty
        elif example == "dead":
            matrix = examples.dead
        elif example == "gosperGliderGun":
            matrix = examples.gosperGliderGun
        elif example == "big":
            matrix = examples.big
        elif example == "big2":
            matrix = examples.big2
    # Use randomGenerator if no matrix has been specified
    if matrix == None:
        rg = randomGenerator.randomGenerator(seed=seed, threshold=threshold, fieldX=dimX, fieldY=dimY)
        matrix = rg.generateMatrix()

    g = game.gameOfLife(matrix, intervall=intervall, trace=trace, gui=gui)
