class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        i=[]
        for y,z in enumerate(words):
            if x in z:
                i.append(y)
        return i