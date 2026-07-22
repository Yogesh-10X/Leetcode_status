class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        x=0
        s=set()
        for y in words:
            if y[::-1] in s:
                x+=1
            s.add(y)
        return x