class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[0]*n
        out[0]=1
        for i in range(1,n):
            out[i]=out[i-1]*nums[i-1]
        
        r=1
        for i in reversed(range(n)):
            out[i]=out[i]*r
            r=r*nums[i]
        
        return out
            
'''
same like the previous approach but optimised
instead of using right array we use a varaible which 
calculates the product of array from right, the output 
array previously has all the left array product values
'''            


            

        