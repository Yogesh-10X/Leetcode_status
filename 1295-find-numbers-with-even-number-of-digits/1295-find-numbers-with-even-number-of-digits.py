class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=co=i=0
        num=nums.copy()
        while num:
            x=nums[i]
            while x>0:
                x//=10
                co+=1
            if co%2==0:
                count+=1 
            co=0 
            num.pop()
            i+=1 
        return count

