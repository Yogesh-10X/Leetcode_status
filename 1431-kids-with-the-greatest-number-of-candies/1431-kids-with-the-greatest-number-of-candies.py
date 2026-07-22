class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        y=max(candies)
        for x in candies:
            if x+extraCandies>=y:
                l.append(True)
            else:
                l.append(False)
        return l