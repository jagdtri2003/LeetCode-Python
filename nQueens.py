class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return
            for col in range(n):
                if not cols[col] and not diag[row+col] and not anti_diag[row-col]:
                    board[row][col] = 'Q'
                    cols[col], diag[row+col], anti_diag[row-col] = True, True, True
                    backtrack(row+1)
                    board[row][col] = '.'
                    cols[col], diag[row+col], anti_diag[row-col] = False, False, False
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols, diag, anti_diag = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        solutions = []
        backtrack(0)
        return solutions