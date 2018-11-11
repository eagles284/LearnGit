import cv2
import time
import heapq

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

        self.weights = {}
    
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

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

# This is now a Priority Queue
class Queue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


# Workspace

map_ml = SquareGrid(map_bg)

def reconstruct_path(came_from, start, goal, vis=False):
    current = goal
    path = []

    while current != start:
        path.append(current)
        if vis:
            map_editable[current[0]][current[1]] = 65
            showPreview()
            time.sleep(0.1)
        current = came_from[0][current]

    path.append(start)  # optional
    path.reverse()  # optional

    return path

def visPath(path, vis=False):
    for p in path:
        map_editable[p[0]][p[1]] = 100
        showPreview()
        time.sleep(0.1)

def heuristic(a, b):
    (y1, x1) = a
    (y2, x2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, goal, vis=False):
    toVisit = Queue()
    toVisit.put(start, 0)

    came_from = {}
    came_from[start] = None

    cost_so_far = {}
    cost_so_far[start] = 0

    while not toVisit.empty():
        currentPos = toVisit.get()

        if vis:
            (y, x) = currentPos
            map_editable[y][x] = 25
            showPreview()

        if(currentPos == goal):
            break

        for visiting in map_ml.neighbors(currentPos):
            new_cost = cost_so_far[currentPos] + map_ml.cost(currentPos, visiting)

            if visiting not in cost_so_far or new_cost < cost_so_far[visiting]:
                cost_so_far[visiting] = new_cost
                priority = new_cost + heuristic(goal, visiting)

                toVisit.put(visiting, priority)
                came_from[visiting] = currentPos
                
    print(str(time.time() - startTime))
    return came_from, cost_so_far

came_from = astar(map_ml, (82, 64), (27, 81), vis=True)
path = reconstruct_path(came_from, (82, 64), (27, 81), vis=False)
visPath(path)