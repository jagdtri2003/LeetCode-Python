"""

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        left,upleft,lowleft=[0]*n,[0]*(2*n-1),[0]*(2*n-1)
        def solve(col,board):
            nonlocal ans
            if col==n:
                ans+=1
                return 
            for row in range(n):
                if not left[row] and not upleft[row+col] and not lowleft[n-1+row-col]:
                    board[row][col]="Q"
                    left[row],upleft[row+col],lowleft[n-1+row-col]=1,1,1
                    solve(col+1,board)
                    board[row][col]="."
                    left[row],upleft[row+col],lowleft[n-1+row-col]=0,0,0
        board=[["." for i in range(n)] for _ in range(n)]
        solve(0,board)
        return ans