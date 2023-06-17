# Final #
## **1.(a)** ##

[1(a)Code](https://github.com/Noircoda/algorithm_final/blob/bc009eeec67ea4f6c57acfac20a50c03f788c274/1/1(a).py)
#### 以上為1(a)code  ####
使用了 defaultdict(list) 的功能:Dictionary來表示有向圖的鄰接表。

使用**DFS**來判斷指定頂點是否為source vertex。在 ` is_source_vertex()` 函式中，建立一個boolean的 visited 列表，用於追蹤每個頂點的訪問狀態。最後，檢查 visited 列表中是否還存在未被訪問的頂點，如果有，則該頂點不是source vertex，否則，該頂點是source vertex。

這個算法的時間複雜度取決頂點數目 (|V|) 和邊的數目 (|E|)。在初始化 visited 列表時，需要 O(|V|) 的時間。在DFS中，最多走訪每個頂點一次，並檢查與之相鄰的邊，這需要 O(|V|+|E|) 的時間。  
因此，總體時間複雜度為 O(2|V| + |E|)=O(|V|+|E|)。   
以下為執行結果
![alt text](pics/1(a)result.jpg "1(a) result")
****************************************************************
## **1.(b)** ##

[1(b)Code](https://github.com/Noircoda/algorithm_final/blob/bc009eeec67ea4f6c57acfac20a50c03f788c274/1/1(b).py)

#### 以上為1(b)code  ####

一樣使用Dictionary來表示有向圖的鄰接表 但是使用**拓樸**的概念

用字典 `in_degree` 來計算每個頂點的in-degree。使用雙向佇列 deque 來實現拓撲排序的過程。首先計算每個頂點的in-degree，然後將in-degree為 0 的頂點加入deque，並依次處理佇列中的頂點。在處理頂點時，將其加入source vertex集合 `sources` 中，同時將與該頂點相鄰的頂點的in-degree減 1，若in-degree減為 0，則將其加入佇列。最後，判斷 sources 是否為空來判斷圖是否包含source vertex。

計算每個頂點的in-degree的時間複雜度為 O(|E|)， |E| 是邊的數量。
拓撲排序的時間複雜度為 O(|V| + |E|)， |V| 是頂點的數量，|E| 是邊的數量。  
因此，整個拓撲排序過程的時間複雜度為 O(|V| + |E|)。  
以下為執行結果
![alt text](pics/1(b)result.jpg "1(b) result")

**********

## **1.(c)** ##  

[1(c)Code](https://github.com/Noircoda/algorithm_final/blob/bc009eeec67ea4f6c57acfac20a50c03f788c274/1/1(c).py)

#### 以上為1(c)code  ####  

由於可能包含有向環，此題使用kosaraju’s algorithm 找出SSC
做兩次DFS time = O(2(|V| + |E|))
時間複雜度為 O(|V| + |E|)

********************************
[回主頁](https://github.com/Noircoda/algorithm_final/blob/82912cf601b3bac25ea72d4023940b8c1a658697)