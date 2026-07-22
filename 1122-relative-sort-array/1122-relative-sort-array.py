class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        z=arr1[:]
        for i in arr2:
            for j in arr1:
                if i==j:
                    l.append(j)
                    z.remove(j)
        z.sort()
        return l+z
                