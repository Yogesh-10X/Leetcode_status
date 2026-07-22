class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        x=0
        y=0
        for n in nums:
            if n>0:
                x+=1
            elif n<0:
                y+=1
        return max(x,y)