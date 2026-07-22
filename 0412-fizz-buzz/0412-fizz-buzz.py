class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num=1
        l=[]
        while num<=n:
            if num%3==0 and num%5==0:
                l.append("FizzBuzz")
            elif num%3==0:
                l.append("Fizz")
            elif num%5==0:
                l.append("Buzz")
            else:
                l.append(str(num))    
            num+=1
        return l
            