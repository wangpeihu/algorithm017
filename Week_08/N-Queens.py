class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #第二种方法：回溯 + 位运算
        def generateBoard():
            board = []
            for i in range(n):
                rows[queens[i]] = "Q"
                board.append("".join(rows))
                rows[queens[i]] = "."
            return board

        def backtrack(row, columns, diagonal1, diagonal2):
            if row == n:
                board = generateBoard()
                res.append(board)
            else:
                avaliablePosition = (
                    ~(columns | diagonal1 | diagonal2)) & ((1 << n) - 1)
                while avaliablePosition:
                    Position = avaliablePosition & (-avaliablePosition)
                    avaliablePosition &= avaliablePosition - 1
                    queens[row] = bin(Position - 1).count("1")
                    backtrack(row + 1, columns | Position, (diagonal1 |
                                                            Position) << 1, (diagonal2 | Position) >> 1)

        res = []
        queens = [-1] * n
        rows = ["."] * n
        backtrack(0, 0, 0, 0)  # backtrack(row, columns, diagonal1, diagonal2)
        return res
