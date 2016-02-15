import getlib
import numpy as np

def checkAdd(gameMap , piece , x , y):
    size_x , size_y = piece.shape
    return x + size_x <= gameMap.shape[0] and y + size_y <= gameMap.shape[1] 

def addPieces(gameMap,piece,x,y):
    newMap =  gameMap.copy()
    newMap[x:x+piece.shape[0],y:y+piece.shape[1]] += piece

    return newMap

def checkDone(gameMap , mod):
    result = gameMap[(gameMap != mod) & ( gameMap != 0)].size == 0
    if (result):
        print(gameMap)
    return result



def dfs(gameMap , pieceIndex , mod):
    global found
    global solution
    global pieces
    global loop

    if pieceIndex >= len(pieces):
        if checkDone(gameMap , mod) :
            found = True
        return 

    loop += 1

    if loop % 10000 == 0 :
        print("Doing %d loops" % loop)

    piece = pieces[pieceIndex]

    for x in range(gameMap.shape[0] - piece.shape[0] + 1):
        for y in range(gameMap.shape[1] - piece.shape[1] + 1):
            if found :
                return 
            tempMap = gameMap.copy()            
            tempMap = addPieces(gameMap , pieces[pieceIndex] , x ,y)
            tempMap[tempMap == mod] = 0
            solution[pieceIndex] = (x,y)
            dfs(tempMap , pieceIndex + 1 , mod)

if __name__ == "__main__":
    while True:
        mission = getlib.getmap()

        loop = 0

        gameMap = np.array([[int(col) for col in row] for row in mission['map']])

        pieces = mission['pieces']
        pieces = [np.array([[int(col == 'X') for col in row] for row in piece.split(',')]) for piece in pieces]

        mod = int(mission['modu'])

        solution = [() for i in range(len(pieces))]

        found = False

        dfs(gameMap , 0 , mod)

        print(solution)

        if found :
            getlib.submit(solution)
        else :
            print("Error")

