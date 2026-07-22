class Solution:
    def reverseWords(self, s: str) -> str:
        x=""
        y=s.split()
        for i in y:
            t=""
            for j in range(len(i)-1,-1,-1):
                t+=i[j]
            x+=t+" "
        return x[:len(x)-1]
