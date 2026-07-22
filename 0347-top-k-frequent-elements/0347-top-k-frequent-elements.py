class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictr = {}
        if len(nums) == len(set(nums)):
            return nums
        for i in nums :
            keyr = i
            if keyr not in dictr : 
                dictr[keyr] = []
            dictr[keyr].append(i)
        val = sorted(dictr.values(), key=len, reverse=True)
        q = 0
        list1=[]
        for i in val :
                list1.append(i[0]) 
                q+=1
                if q == k :
                    break
        return list1