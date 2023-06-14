## 3. ##
[code](https://github.com/Noircoda/algorithm_final/blob/main/2/3.py)

在此題中，使用了以下資料結構：

1. 二維陣列 `e`：用於存儲子問題的期望成本。`e[i][j]` 表示包含鍵 `ki` 到 `kj` 和dummy key `di-1` 到 `dj` 的最佳二元搜尋樹的期望成本。

2. 二維陣列 `w`：用於存儲子問題的機率(權重)。`w[i][j]` 表示包含鍵 `ki` 到 `kj` 和dummy key `di-1` 到 `dj` 的子樹的機率(權重)。

3. 二維陣列 `root`：用於存儲子問題的根節點位置。`root[i][j]` 表示包含鍵 `ki` 到 `kj` 和dummy key `di-1` 到 `dj` 的子樹的root位置。


### **Time complexity：**
時間複雜度為 **O(n^3)**， n = 鍵的數量。因為使用了兩個迴圈來填入 `e` 和 `w` 陣列，迴圈的次數是 n^2。在內部迴圈，又用了一個迴圈來計算 `e[i][j]` 的值，迴圈的次數也是 n。因此，總共的時間複雜度為 O(n^3)。

### **Space complexity：**
空間複雜度為 **O(n^2)**，因為需要使用大小為 n+2 的二維陣列 `e` 和 `w` 以及大小為 n+1 的二維陣列 `root`。這些array使用了 O(n^2) 的額外空間。