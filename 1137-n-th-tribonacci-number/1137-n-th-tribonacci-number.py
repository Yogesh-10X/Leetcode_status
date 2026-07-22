class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=c=1
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        while n>2:
            z=a+b+c
            a,b,c=b,c,z
            n-=1
        return z