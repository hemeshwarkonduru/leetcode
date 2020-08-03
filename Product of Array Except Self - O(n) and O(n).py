class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r,out=[0]*len(nums),[0]*len(nums),[0]*len(nums)
        l[0]=1
        r[len(nums)-1]=1
        n=len(nums)
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        
        r[n-1]=1
        for i in reversed(range(n-1)):
            r[i]=r[i+1]*nums[i+1]
        
        for i in range(n):
            out[i]=l[i]*r[i]
        
        return out

'''
left array has values where 'i'th value represents 
its product from left till that index and vice versa to roght array

for output array we find the product of the left and right array
'''