""""
        Recursion + DP 
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(row,col,dp):
            if row==m-1 or col==n-1: #Agar Last Row Ya Column me honge toh ik hi rasta hoga bss 
                return 1
                
            if dp.get((row,col)):
                return dp[(row,col)]

            dp[(row,col+1)]=solve(row,col+1,dp)         #Using DP to Store
            dp[(row+1,col)]=solve(row+1,col,dp)
        
            return dp[(row,col+1)] + dp[(row+1,col)]
        
        ans=solve(0,0,{})
        return ans