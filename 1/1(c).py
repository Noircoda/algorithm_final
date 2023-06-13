def has_source_vertex(graph):
    for vertex in graph:
        visited = set()

        # 使用深度优先搜索遍历图
        stack = [vertex]
        while stack:
            current = stack.pop()
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

        if len(visited) != len(graph):
            return False

    return True

# 测试代码
graph = {
    1: [2],
    2: [3],
    3: [4],
    4: [1],
    5: []
}
print(has_source_vertex(graph))  # 预期输出: False

graph = {
    1: [2],
    2: [3],
    3: [4],
    4: [1],
    5: [4]
}
print(has_source_vertex(graph))  # 预期输出: True
