import collections

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]
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

graf = SimpleGraph()
graf.edges = {'Arya': ['Faiz'],
              'Faiz': ['Dhika', 'Aqqil', 'Sigit', 'Aziz', 'Arya', 'Faisal'],
              'Faisal': ['Rendy', 'Salman', 'Aril', 'Arya'],
              'Aqqil': ['Alvis', 'Dhika', 'Faiz'],
              'Dhika': ['Sigit', 'Aziz'],
              'Rendy': ['Salman'],
              'Salman': ['Rendy', 'Faisal'],
              'Sigit': ['Aziz'],
              'Aziz': ['Sigit'],
              'Alvis': ['Aqqil', 'Arya', 'Faisal'],
              'Aril': ['Sigit']}

def visit(graph, start):
    visited = {}
    visited[start] = True
    toVisit = Queue()
    toVisit.put(start)

    while not toVisit.empty():
        currentPeople = toVisit.get()

        for neighbor in graf.neighbors(currentPeople):
            if neighbor not in visited:
                print('Visiting %r' % neighbor)
                visited[neighbor] = True
                toVisit.put(neighbor)

visit(graf, 'Arya')








