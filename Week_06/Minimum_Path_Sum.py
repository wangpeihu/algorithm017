#DP方程：sum(i,j) = a(i, j) + min(sum(i, j + 1), sum(i + 1, j)) 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # i -> rows, j -> columns
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    
        return dp[rows - 1][columns - 1]