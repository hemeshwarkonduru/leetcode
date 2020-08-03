

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}        
        for i in range(len(nums)):
            if((target-nums[i]) in s.keys()):#s.keys is to check all the keys in dictionary
                return [s[target-nums[i]],i] 
            s[nums[i]]=i #update the number always to i to print the index of it as list

