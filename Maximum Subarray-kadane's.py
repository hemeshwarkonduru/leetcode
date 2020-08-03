class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        local=nums[0]
        su=nums[0]
#using kadane's algorithm we find local sum till the index value and 
#compare with its own index value we assign it to maxi 
#refer youtube on kadane's algo
        for i in range(1,len(nums)):
            su+=nums[i]
            local=max(su,nums[i])
            if(local==nums[i]):
                su=nums[i]
            if(local > maxi):
                maxi=local
                
        
        return maxi