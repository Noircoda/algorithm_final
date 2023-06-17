from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def dfs_reverse(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_reverse(i, visited, result)

    def get_transpose(self):
        g_reverse = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g_reverse.add_edge(j, i)
        return g_reverse

    def get_scc(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)
        
        g_reverse = self.get_transpose()
        
        visited = [False] * self.V
        scc = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                result = []
                g_reverse.dfs_reverse(v, visited, result)
                scc.append(result)
        return scc

    def has_source_vertex(self):
        scc = self.get_scc()
        if len(scc) == 1:
            return True
        return False
# test
g = Graph(5)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.has_source_vertex():
    print("The graph has a source vertex.")
else:
    print("The graph does not have a source vertex.")
