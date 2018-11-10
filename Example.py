import cv2
import numpy as np
import time
from CV_ASTAR import astar

multi = 1

img = cv2.imread('res/map_rendering/map_canny_145.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, None,fx=multi, fy=multi, interpolation=cv2.INTER_NEAREST)

map_img = cv2.imread('res/map_rendering/map_canny_145.png')
map_img = cv2.cvtColor(map_img, cv2.COLOR_BGR2GRAY)
map_img = cv2.resize(map_img, None,fx=multi, fy=multi, interpolation=cv2.INTER_NEAREST)
5
lastPos = [0, 0]
pos = [0, 0]

startTime = time.time()


def move(paths):
    for p in paths:

        if p == 'moveRightDown()':
            moveRightDown()
        if p == 'moveRightUp()':
            moveRightUp()
        if p == 'moveLeftDown()':
            moveLeftDown()
        if p == 'moveLeftUp()':
            moveLeftUp()

        if p == 'moveRight()':
            moveRight()
        if p == 'moveLeft()':
            moveLeft()
        if p == 'moveUp()':
            moveUp()
        if p == 'moveDown()':
            moveDown()

def ce(x, y):
    xy = (y, x)
    return xy

def drawPosition():
    global img, pos, lastPos
    # time.sleep(1)
    img[ce(pos[0], pos[1])] = 128

    preview = cv2.resize(img, None,fx=3/multi, fy=3/multi, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Mapping', preview)
    if (cv2.waitKey(25) & 0xFF == ord('q')):
        cv2.destroyAllWindows()
    time.sleep(0.1)

def updateLastPosition():
    global lastPos, pos
    lastPos = pos
    img[ce(lastPos[0], lastPos[1])] = map_img[ce(lastPos[0], lastPos[1])]


def moveDown():
    global pos
    updateLastPosition()
    pos[1] += 1
    drawPosition()
def moveRight():
    global pos
    updateLastPosition()
    pos[0] += 1
    drawPosition()
def moveLeft():
    global pos
    updateLastPosition()
    pos[0] += -1
    drawPosition()
def moveUp():
    global pos
    updateLastPosition()
    pos[1] += -1
    drawPosition()

def moveRightUp():
    global pos
    updateLastPosition()
    pos[0] += 1
    pos[1] += -1
    drawPosition()

def moveRightDown():
    global pos
    updateLastPosition()
    pos[0] += 1
    pos[1] += 1
    drawPosition()
def moveLeftUp():
    global pos
    updateLastPosition()
    pos[0] += -1
    pos[1] += -1
    drawPosition()
def moveLeftDown():
    global pos
    updateLastPosition()
    pos[0] += -1
    pos[1] += 1
    drawPosition()

def generateMoves(p):
    p = tuple(p)

    moves = []
    i = 0

    for i in range(len(p)-2):
        
        curY = p[i][0]
        nexY = p[i+1][0]
        
        curX = p[i][1]
        nexX = p[i+1][1]

        if (curY < nexY) & (curX < nexX):
            moves.append('moveRightDown()')
        if (curY > nexY) & (curX < nexX):
            moves.append('moveRightUp()')
        if (curY > nexY) & (curX > nexX):
            moves.append('moveLeftUp()')
        if (curY < nexY) & (curX > nexX):
            moves.append('moveLeftDown()')
        if (curY == nexY) & (curX < nexX):
            moves.append('moveRight()')
        if (curY == nexY) & (curX > nexX):
            moves.append('moveLeft()')
        if (curY > nexY) & (curX == nexX):
            moves.append('moveUp()')
        if (curY < nexY) & (curX == nexX):
            moves.append('moveDown()')
        i += 1

    print('Time needed: ', time.time() - startTime, '\nLength: ', len(p))
    return moves

def movefromab(yx1, yx2):
    global pos
    pos = [yx1[1], yx1[0]]

    path = astar(list(map_img), (yx1[0], yx1[1]), (yx2[0], yx2[1]))
    moves = generateMoves(path)
    print(path)
    print(moves)
    move(moves)

# Y, X <= 450
startPos = (int(140*multi), int(6*multi))

endPos = (int(98*multi), int(84*multi))

# endPos = (int(120*multi), int(24*multi))

movefromab(startPos, endPos)