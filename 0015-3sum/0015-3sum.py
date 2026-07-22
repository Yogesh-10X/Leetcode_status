class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            y=i+1
            z=len(nums)-1
            while y<z:
                if nums[i]+nums[y]+nums[z]==0:
                    l.append([nums[i],nums[y],nums[z]])
                    y+=1
                    z-=1
                    while y < z and nums[y] == nums[y-1]:
                        y += 1
                    while y < z and nums[z] == nums[z+1]:
                        z -= 1
                elif nums[i]+nums[y]+nums[z]<0:
                    y+=1
                elif nums[i]+nums[y]+nums[z]>0:
                    z-=1
        return l   