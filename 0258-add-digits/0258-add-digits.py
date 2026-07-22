class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        if num==0:
            return 0
        while num!=0:
            x=num%10
            s+=x
            num//=10
            if num==0 :
                if s//10==0:
                    return s
                else :
                    num=s
                    s=0



