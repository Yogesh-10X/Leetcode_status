class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=nums[n:]
        q=nums[:n]        
        l1=[]
        for i in range(n):
            l1.append(q[i])
            l1.append(l[i])
        return l1