from sys import stdin
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def gera_vizinho(self,v):
        for k in self.graph[v]:
            yield k

    def nonRecursiveTopologicalSortUtil(self, v, visited, stack):
        working_stack = [(v, self.gera_vizinho(v))]
        while len(working_stack) > 0:
            v, gen = working_stack[-1]
            visited[v] = True
            working_stack.pop()
            continue_flag = True
            while continue_flag:
                next_neighbor = next(gen,None)
                if next_neighbor is None:
                    continue_flag = False
                    stack.append(v)
                    continue
                if not(visited[next_neighbor]):
                    working_stack.append((v,gen))
                    working_stack.append((next_neighbor,self.gera_vizinho(next_neighbor)))
                    continue_flag = False

    def nonRecursiveTopologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if not(visited[i]):
                self.nonRecursiveTopologicalSortUtil(i, visited, stack)
        stack = [x+1 for x in stack]
        print(' '.join(map(str, reversed(stack))))

while True:
    x, y = list(map(int, stdin.readline().split()))
    if x == 0 and y == 0:
        break
    grafo = Graph(x)
    for _ in range(y):
        i, j = list(map(int, stdin.readline().split()))
        grafo.add_edge(i-1, j-1)
    grafo.nonRecursiveTopologicalSort()
