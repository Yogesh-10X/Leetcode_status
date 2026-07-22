class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        list1=[1]*n
        left = 1
        for i in range(n):
            list1[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            list1[i] *= right 
            right *= nums[i]
        return list1     