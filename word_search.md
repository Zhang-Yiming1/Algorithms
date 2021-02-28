#### [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
```




提示：

- board 和 word 中只包含大写和小写英文字母。
- 1 <= board.length <= 200
- 1 <= board[i].length <= 200
- 1 <= word.length <= 10^3

### 官方题解

先审题，题目给定一个二维数组和一个单词，需要求出单词是否存在于网格中。

其中判断单词是否存在于二维数组中的依据是：

- 单词存在于二维数组必须是按照字母顺序，且构建单词字母必须是相邻单元格（相邻单元格表示当前单元格四个方位相邻的其他单元格）
- 同个单元格的字母不能重复使用。



那么，我们可以发现要去判断单词是否存在于二维数组中，首先我们需要先找到单词的起始字母，然后再向四周扩散搜索。具体的思路如下：

- 默认从坐标 (0, 0) 开始搜索，先找到单词首字母，然后对其先进行标记（防止同个单元格被重复使用）；
- 然后向四个方位进行扩散搜索（注意限定边界，以及注意是否已被标记），对单元格的字母与单词中的字母继续比对：
  - 若匹配，则进行标记，继续扩散搜索；
  - 若不匹配，则尝试其他方位；
  - 若完全不匹配（四个方位都不匹配），则进行回退，同时释放当前单元格的标记。

重复上面的步骤：

- 当单词完全匹配，可直接返回 True；
- 若所有单元格均搜索无果，则返回 False。

![](https://pic.leetcode-cn.com/1599981006-zQigOS-79_%E5%8D%95%E8%AF%8D%E6%90%9C%E7%B4%A2.gif)



### 官方代码

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [[False] * n for _ in range(m)]

        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]

        def dfs(x, y, idx):
            """搜索单词
            Args:
                x: 行索引
                y: 列索引
                idx: 单词对应的字母索引
            """
            if board[x][y] != word[idx]:
                return False
            
            if idx == len(word) - 1:
                return True
            
            # 先标记
            visited[x][y] = True

            # 找到符合的字母时开始向四个方向扩散搜索
            for i in range(4):
                nx = x + rows[i]
                ny = y + cols[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and dfs(nx, ny, idx+1):
                        return True
            # 扩散未搜索对应的字母，释放标记
            # 继续往其他方位搜索
            visited[x][y] = False
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        
        return False


```

作者：yiluolion
链接：https://leetcode-cn.com/problems/word-search/solution/79-dan-ci-sou-suo-dfs-hui-su-by-yiluolion/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。