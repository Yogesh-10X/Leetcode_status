class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        c=0
        l=[]
        for i in range(left,right+1):
            z=i
            while i>0:
                x=i%10
                if x!=0 and z%x==0:
                    i//=10
                    if i==0:
                        l.append(z)
                else:
                    break
        return l

        