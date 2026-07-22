class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
            l2=[]
            l3=[]
            for i in nums:
                if i%2==0:
                    l2.append(i)
                else:
                    l3.append(i)
            return l2+l3