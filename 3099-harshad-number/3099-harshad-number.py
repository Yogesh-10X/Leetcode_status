class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        z=x
        while x>0:
            n=x%10
            s+=n
            x//=10
        if z%s==0:
            return s
        return -1