class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        a=0
        while n>0:
            x=n%10
            p*=x
            a+=x
            n//=10
        return p-a

