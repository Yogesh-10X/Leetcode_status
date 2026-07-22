class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        y=[]
        z=nums.copy()
        i=0
        while z:
            if i==0:
                y.append(nums[i])
            else:
                y.append(y[i-1]+nums[i])
            z.pop()
            i+=1
        return y