

## **2.(a)** ##

[ford_fulkerson](https://github.com/Noircoda/algorithm_final/blob/main/2/ford_fulkerson.py)
### 以上為2(a)code  ###
使用了 adjacency matrix 來表示graph。

本題利用Ford-Fulkerson演算法，解決maximum flow問題。

首先定義一個Graph類別，包含以下方法：
- `BFS(self, s, t, parent)`: 實現廣度優先搜索(BFS)算法，用於找到從源節點s到目標節點t的路徑。
- `parent`是一個陣列，用於儲存搜尋過程中的父節點。
- `FordFulkerson(self, source, sink)`: 實現Ford-Fulkerson演算法，計算從source到sink的最大流量。
    

以下為執行結果
![alt text](pics/2(a)result.jpg "2(a) result")  
$$故得maximum flow為30$$
****************************************************************
## **2.(b)** ##  

本題一樣利用Ford-Fulkerson演算法，每次找到增廣路徑後，將該增廣路徑印出。  
Ford-Fulkerson Algorithm的方法如下：

1. 在Residual Networks上尋找Augmenting Paths。
2. 若以BFS()尋找，便能確保每次找到的Augmenting Paths一定經過「最少的edge」。
3. 找到Augmenting Paths上的「最小residual capacity」加入總flow。
4. 再以「最小residual capacity」更新Residual Networks上的edge之residual capacity。
5. 重複上述步驟，直到再也沒有Augmenting Paths為止。

以下為執行結果
![alt text](pics\augmenting_path.jpg "augmenting_path")

### 再來求最小的s-t cut ###
minimium cut = maximum flow=**4**
