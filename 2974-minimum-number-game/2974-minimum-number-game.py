class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        x=[]
        for i in range(0,len(nums),2):
            x.append(nums[i+1])
            x.append(nums[i])
        return x    