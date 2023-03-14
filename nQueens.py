"""
                    BackTracking 
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        def is_safe(row,col,board):
            dcol=col
            while dcol>=0:
                if board[row][dcol]=="Q":
                    return False
                dcol-=1
            dcol,drow=col,row
            while dcol>=0 and drow>=0:
                if board[drow][dcol]=="Q":
                    return False
                drow-=1
                dcol-=1
            dcol,drow=col,row
            while dcol>=0 and drow<n:
                if board[drow][dcol]=="Q":
                    return False
                drow+=1
                dcol-=1
            return True
        
        def solve(col,board):
            if col==n:
                ans.append(["".join(i) for i in board])
                return 
            for row in range(n):
                if is_safe(row,col,board):
                    board[row][col]="Q"
                    solve(col+1,board)
                    board[row][col]="."                     #BackTrack
        board=[["." for _ in range(n)] for i in range(n)]
        solve(0,board)
        return ans

            

"""
                        -> Optimized Solution 

We don't use need to use is_safe function instead we maintain an array for left,upper left and lower left 


"""



class Solution(object):
    def solveNQueens(self, n):
        left,upleft,lowleft=[0]*n,[0]*(2*n-1),[0]*(2*n-1)
        ans=[]
        def solve(col,board):
            if col==n:
                ans.append(["".join(i) for i in board])
                return 
            for row in range(n):
                if not left[row] and not upleft[n-1+row-col] and not lowleft[row+col]:
                    board[row][col]="Q"
                    left[row]=1
                    upleft[n-1+row-col]=1
                    lowleft[row+col]=1
                    solve(col+1,board)
                    board[row][col]="."                         #Backtrack
                    left[row]=0
                    upleft[n-1+row-col]=0
                    lowleft[row+col]=0
        board=[["." for i in range(n)] for _ in range(n)]
        solve(0,board)
        return ans
