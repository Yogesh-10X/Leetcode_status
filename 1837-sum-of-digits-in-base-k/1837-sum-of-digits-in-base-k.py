class Solution:
    def sumBase(self, n: int, k: int) -> int:
        y=1
        x=0
        while y!=0:
            y=n//k
            z=n%k
            n=y
            x+=z  
        return x      

