class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        maxside = max([max(dp[i]) for i in range(rows)])
        return maxside * maxside