from collections import deque

def has_source_vertex(graph):
    in_degree = {v: 0 for v in graph}
    queue = deque()

    # 計算每個頂點的in-degree
    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    # 將in-degree為 0 的頂點加入佇列
    for v in graph:
        if in_degree[v] == 0:
            queue.append(v)

    sources = set()

    # 拓撲排序
    while queue:
        vertex = queue.popleft()
        sources.add(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(sources) > 0

# 測試
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(has_source_vertex(graph))  # True

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['A']  
}

print(has_source_vertex(graph))  # False