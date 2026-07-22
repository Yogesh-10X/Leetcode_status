class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for x in s:
            if x in["(","[","{"]:
                l.append(x)
            else:
                if len(l)==0:
                    return False
                y=l.pop()
                if x==")" and y!="(":
                    return False
                if x=="]" and y!="[":
                    return False
                if x=="}" and y!="{":
                    return False
        return len(l)==0
