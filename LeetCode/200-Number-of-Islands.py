class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[i]) and grid[x][y] != '0':
                    dfs(x, y)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count