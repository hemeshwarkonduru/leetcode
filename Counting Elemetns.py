class Solution:
    def countElements(self, arr: List[int]) -> int:
        s=set()
        for i in range(len(arr)):
            if(arr[i] not in s):
                s.add(arr[i])
        c=0
        for i in range(len(arr)):
            if((arr[i]+1) in s):
                c+=1
        
        return c
            