class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in sentences:
            y=len(i.split())
            if y>count:
                count=y
        return count