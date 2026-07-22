class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        r=0
        while x>0:
            z=x%10
            r=r*10+z
            x//=10
        if r==y:
            return True
        else:
            return False