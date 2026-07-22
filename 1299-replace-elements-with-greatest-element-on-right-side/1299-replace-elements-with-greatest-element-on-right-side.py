class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        z=-1
        for i in range (len(arr)-1,-1,-1):
            x=arr[i]
            arr[i]=z
            z=max(x,z)
        return arr

