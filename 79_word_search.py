class Solution:
    def exist(board, word):
        # board: List[List[str]], word: str
        '''
        [["a","b"]]
        "ba"
        输出：false
        预期结果：true
        '''
        # m: board 行数

        m = len(board)
        # n: board 列数
        n = len(board[0])
        # 重要的一点 # 建立一个二维数组记录元素是否被访问
        visited = [[False] * n for _ in range(m)]
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]

        def dfs(x, y, idx):
            '''
            x: 行的索引
            y: 列的索引
            rows :行
            cols :列
            [-1, 0]: 向左移动一格
            [0, 1]:  向下移动一格
            [1, 0]:  向右移动一格
            [0, -1]: 向上移动一格
            '''

            if board[x][y] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

                # 先标记 ,这个位置很重要！！！
            visited[x][y] = True

            # 先向4个方向扩散搜索
            for i in range(len(rows)):
                nx = x + rows[i]
                ny = y + cols[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and dfs(nx, ny, idx + 1):
                    return True
            visited[x][y] = False  # 四个方向都不满足，释放标记
            # 往其他方向继续搜索
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


if __name__ == '__main__':
    board =  [["a","b"]]
    word = "ba"
    print(Solution.exist(board, word))
