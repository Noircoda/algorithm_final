from collections import deque

class Graph_FlowNetWorks:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.adj_matrix = [[0] * num_vertex for _ in range(num_vertex)]

    def add_edge(self, from_vertex, to_vertex, capacity):
        self.adj_matrix[from_vertex][to_vertex] = capacity

    def bfs_find_existing_path(self, graph, predecessor, source, termination):
        visited = [0] * self.num_vertex
        queue = deque()

        queue.append(source)
        visited[source] = 1

        while queue:
            exploring = queue.popleft()
            for j in range(self.num_vertex):
                if graph[exploring][j] != 0 and visited[j] == 0:
                    queue.append(j)
                    visited[j] = 1
                    predecessor[j] = exploring

        return visited[termination] == 1

    def min_capacity(self, graph, predecessor, termination):
        min_capacity = 100  # 假設所有容量都小於100

        for idx in range(termination, -1, -1):
            if predecessor[idx] != -1 and graph[predecessor[idx]][idx] != 0 and graph[predecessor[idx]][idx] < min_capacity:
                min_capacity = graph[predecessor[idx]][idx]

        return min_capacity


    def ford_fulkerson(self, source, termination):
        graph_residual = [row[:] for row in self.adj_matrix]
        max_flow = 0
        predecessor = [-1] * self.num_vertex

        while self.bfs_find_existing_path(graph_residual, predecessor, source, termination):
            min_capacity = self.min_capacity(graph_residual, predecessor, termination)
            max_flow += min_capacity

            Y = termination
            augmenting_path = [Y]
            while Y != source:
                X = predecessor[Y]
                graph_residual[X][Y] -= min_capacity
                graph_residual[Y][X] += min_capacity
                augmenting_path.append(X)
                Y = predecessor[Y]

            augmenting_path.reverse()
            print("Augmenting Path:", augmenting_path)

        print("Possible Maximum Flow:", max_flow)
    
    def find_minimum_cut(self, source, termination):
        visited = [False] * self.num_vertex
        self.dfs(visited, source)

        min_cut = []
        for i in range(self.num_vertex):
            if visited[i]:
                min_cut.append(i)

        return min_cut

    def dfs(self, visited, vertex):
        visited[vertex] = True

        for i in range(self.num_vertex):
            if not visited[i] and self.adj_matrix[vertex][i] > 0:
                self.dfs(visited, i)


if __name__ == "__main__":
    g11 = Graph_FlowNetWorks(6)

    g11.add_edge(0, 1, 5)
    g11.add_edge(1, 0, 7)
    g11.add_edge(0, 2, 4)
    g11.add_edge(0, 2, 7)
    g11.add_edge(1, 3, 1)
    g11.add_edge(3, 3, 9)
    g11.add_edge(2, 1, 3)
    g11.add_edge(1, 2, 2)
    g11.add_edge(2, 4, 1)
    g11.add_edge(4, 2, 7)
    g11.add_edge(3, 2, 3)
    g11.add_edge(2, 3, 2)
    g11.add_edge(3, 5, 1)
    g11.add_edge(5, 3, 2)
    g11.add_edge(4, 3, 12)
    g11.add_edge(3, 4, 7)
    g11.add_edge(4, 5, 8)
    g11.add_edge(5, 4, 12)

    g11.ford_fulkerson(0, 5)
    min_cut = g11.find_minimum_cut(0, 5)
    print("Minimum Cut:", min_cut)
