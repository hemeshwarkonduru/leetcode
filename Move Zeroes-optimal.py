class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        i=1
        while(i<len(nums)):
            if(nums[i]!=0 and nums[j]==0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif(nums[i]==0 and nums[j]==0):
                i+=1
            else:
                i+=1
                j+=1

                
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        j=0
        for i in range(len(nums)):
 
                
            if( nums[i]!=0):
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
"""
            
