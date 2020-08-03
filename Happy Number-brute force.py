nums=[8,-19,5,-4,20]
maxi=nums[0]
local=nums[0]
su=nums[0]
for i in range(1,len(nums)):
    su+=nums[i]
    print(su)
    local=max(su,nums[i])
    print(local)
    if(local > maxi):
        maxi=local
        su=local

print(maxi)