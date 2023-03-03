def subSequence(arr,n):
    ans=[]
    def rec(idx,lst):
        if idx>=n:
            ans.append(lst)
            return 
        rec(idx+1,lst)                      #Not Take 
        rec(idx+1,lst+[arr[idx]])           #Take 
    rec(0,[])
    return ans

arr1=[3,2,1]
a=subSequence(arr1,3)
print(a)