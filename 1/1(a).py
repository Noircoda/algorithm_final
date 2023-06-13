from collections import defaultdict

def is_source_vertex(V, E, v):
    graph = defaultdict(list)

    for u, v in E:
        graph[u].append(v)

    visited = [False] * len(V)

    def dfs(vertex):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(v)

    if any(not visited[i] for i in range(len(V))):
        return False
    else:
        return True

# 測試程式碼
if __name__ == '__main__':
    V = [0, 1, 2, 3, 4]
    E = [(0, 1), (1, 2), (2, 3), (3, 4)]

    if is_source_vertex(V, E, 0):
        print("頂點0是source vertex")
    else:
        print("頂點0不是source vertex")
