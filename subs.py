"""
                                        GFG

Given an array S consisting of N numbers, find the sum of difference between last and first element of each subset.


"""
def sumDiff(S, n):
    #Code here
    ans=0
    def solve(idx,lst):
        nonlocal ans
        if idx>=n:
            if len(lst)>0:
                ans+=lst[-1]-lst[0]
            return 
        solve(idx+1,lst)
        solve(idx+1,lst+[S[idx]])
    solve(0,[])
    return ans

print(sumDiff([5,8,7],3))