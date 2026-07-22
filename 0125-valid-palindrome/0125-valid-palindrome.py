class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=""
        for i in s:
            if i.isalnum():
                w+=i.lower()
        return w==w[::-1]
