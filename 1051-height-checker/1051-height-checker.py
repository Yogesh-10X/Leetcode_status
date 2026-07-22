class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        h1=heights[:]
        x=sorted(heights)
        for i in range(len(h1)):
            if h1[i]!=x[i]:
                count+=1
        return count
            

