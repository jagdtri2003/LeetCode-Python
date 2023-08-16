"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
 
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(idx,target,dp):
            if idx==0:
                if target%coins[0]==0: #Check krenge agr divide hoga tb required return krdenge wrna ik bdi value
                    return target/coins[0]
                return 1e9
            
            if dp.get((idx,target)):            #Using DP
                return dp.get((idx,target))

            not_take=0+solve(idx-1,target,dp)   #Not Taking the denomination , so idx-1 ho jayega but target will be same 
            # Ab nhi lenge toh count nhi hoga isileye 0+
            take=float('inf')

            if coins[idx]<=target:
                take=1+solve(idx,target-coins[idx],dp)      #Taking the denomination , so idx wahi rhega but target reduce ho jayega
            # Ab lenge toh count hoga isileye 1+

            dp[(idx,target)]=min(not_take,take)     #Add result to DP
            
            return dp[(idx,target)]
        
        ans=solve(len(coins)-1,amount,{})
        if ans!=1e9:
            return int(ans)
        return -1
