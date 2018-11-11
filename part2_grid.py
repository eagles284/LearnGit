import cv2
import time
import collections

map_bg = cv2.imread('map.png')
map_bg = cv2.cvtColor(map_bg, cv2.COLOR_BGR2GRAY)
map_editable = cv2.imread('map.png')
map_editable = cv2.cvtColor(map_editable, cv2.COLOR_BGR2GRAY)

startTime = time.time()

def showPreview():
    preview = cv2.resize(map_editable, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Mapping', preview)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.destroyAllWindows()

# (Y, X) Format !!!
class SquareGrid:
    def __init__(self, image):
        self.img = image
        self.width = len(image[0]) - 1
        self.height = len(image) - 1
    
    def in_bounds(self, id):
        (y, x) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return self.img[id[0]][id[1]] <= 26
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x+y) % 2 == 0:
            results = list(reversed(results))
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()


# Workspace

map_ml = SquareGrid(map_bg)

def breadth_first(grid, start):
    came_from = {}
    came_from[start] = None

    toVisit = Queue()
    toVisit.put(start)

    while not toVisit.empty():
        currentPos = toVisit.get()

        (y, x) = currentPos
        map_editable[y][x] = 25
        showPreview()

        for neighbor in map_ml.neighbors(currentPos):

            if neighbor not in came_from:
                came_from[neighbor] = currentPos
                toVisit.put(neighbor)
                
    print(str(time.time() - startTime))
    return came_from

breadth_first(map_ml, (42, 59))








