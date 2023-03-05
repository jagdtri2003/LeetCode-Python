def subSequence(arr):
    n=len(arr)
    ans=[]
    def rec(idx,lst):
        if idx>=n:
            ans.append(lst)
            return 
        rec(idx+1,lst)                      #Not Take 
        rec(idx+1,lst+[arr[idx]])           #Take 
    rec(0,[])
    return ans

def subSequenceWithSum(arr,sum):
    n=len(arr)
    ans=[]
    def dfs(idx,lst,total):
        if idx>=n:
            if total==sum:
                ans.append(lst)
            return 
        dfs(idx+1,lst,total)
        dfs(idx+1,lst+[arr[idx]],total+arr[idx])
    
    dfs(0,[],0)
    return ans


arr1=[3,2,1,1,2,1]
a=subSequence(arr1)
b=subSequenceWithSum(arr1,3)
print(b)
# print(a)