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