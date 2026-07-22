class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=int(num**0.5)
        if n**2==num:
            return True
        else:
            return False

