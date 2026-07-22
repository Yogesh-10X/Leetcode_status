class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        l,r=0,len(x)-1
        while l<r:
            x[l],x[r]=x[r],x[l]
            l+=1
            r-=1
        return " ".join(x)