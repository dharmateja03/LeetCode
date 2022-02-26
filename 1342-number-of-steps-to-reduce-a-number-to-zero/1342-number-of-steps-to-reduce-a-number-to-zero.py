class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while(num):
            if not num%2:
                num=num//2
                c+=1
            else:
                c+=1
                num-=1
        return c
        