"""
                Recursion 
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def solve(idx,lst):
            if idx>=n:
                ans.append(lst)
                return 
            solve(idx+1,lst)                    #Not Taking
            solve(idx+1,lst+[nums[idx]])        #Taking 
        solve(0,[])
        return ans