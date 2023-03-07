class Solution:
    def nQueen(self, n):
        # code here
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
            
        def solve(col,board,pos):
            if col==n:
                ans.append(pos)
                return 
            for row in range(n):
                if is_safe(row,col,board):
                    board[row][col]="Q"
                    solve(col+1,board,pos+[row+1])
                    board[row][col]="."
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0,board,[])
        return ans