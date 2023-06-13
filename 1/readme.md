# Final #
## **1.(a)** ##

```python
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

```

### 以上為1(a)code  ###
使用了 defaultdict(list) 的功能:Dictionary來表示有向圖的鄰接表。

使用**DFS**來判斷指定頂點是否為source vertex。在 ` is_source_vertex()` 函式中，建立一個boolean的 visited 列表，用於追蹤每個頂點的訪問狀態。最後，檢查 visited 列表中是否還存在未被訪問的頂點，如果有，則該頂點不是source vertex，否則，該頂點是source vertex。

這個算法的時間複雜度取決頂點數目 (|V|) 和邊的數目 (|E|)。在初始化 visited 列表時，需要 O(|V|) 的時間。在DFS中，最多走訪每個頂點一次，並檢查與之相鄰的邊，這需要 O(|V|+|E|) 的時間。  
因此，總體時間複雜度為 O(2|V| + |E|)=O(|V|+|E|)。   
以下為執行結果
![alt text](pics/1(a)result.jpg "1(a) result")
****************************************************************
## **1.(b)** ##

``` python
from collections import deque

def has_source_vertex(graph):
    in_degree = {v: 0 for v in graph}
    queue = deque()


    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    # in-degree=0 的頂點加入queue
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
    'D': ['A']  # 含有向循環
}

print(has_source_vertex(graph))  # False
```

### 以上為1(b)code  ###

一樣使用Dictionary來表示有向圖的鄰接表 但是使用**拓樸**的概念

用字典 `in_degree` 來計算每個頂點的in-degree。使用雙向佇列 deque 來實現拓撲排序的過程。首先計算每個頂點的in-degree，然後將in-degree為 0 的頂點加入deque，並依次處理佇列中的頂點。在處理頂點時，將其加入source vertex集合 `sources` 中，同時將與該頂點相鄰的頂點的in-degree減 1，若in-degree減為 0，則將其加入佇列。最後，判斷 sources 是否為空來判斷圖是否包含source vertex。

計算每個頂點的in-degree的時間複雜度為 O(|E|)， |E| 是邊的數量。
拓撲排序的時間複雜度為 O(|V| + |E|)， |V| 是頂點的數量，|E| 是邊的數量。  
因此，整個拓撲排序過程的時間複雜度為 O(|V| + |E|)。  
以下為執行結果
![alt text](pics/1(b)result.jpg "1(b) result")

**********

## **1.(c)** ##
```python

```
由於可能包含有向環，此題使用DFS
