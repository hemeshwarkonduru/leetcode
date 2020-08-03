class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m={}# using maps we can keep count of occurences
        for i in nums:
            if(i in m):
                m[i]+=1
                continue 
            m[i]=1
        
        for k,v in m.items():
            if(v==1):
                return k
        
        return -1
            

            
                
        