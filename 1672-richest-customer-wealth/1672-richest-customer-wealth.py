class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=0
        rich=0
        for n in accounts:
            for i in n:
                sum+=i
            if sum>rich:
                rich=sum
            sum=0
        return rich
