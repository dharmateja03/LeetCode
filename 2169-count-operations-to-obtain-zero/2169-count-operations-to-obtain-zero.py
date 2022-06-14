class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        #10 7 - 
        #37 - 34- 31 -21 -11-01
        c=0
        if not num1 or not num2:
            return 0
        while(num1!=1 or num2!=1):
            if num1>num2:
                c+=1
                num1-=num2
            elif num2>num1:
                c+=1
                num2-=num1
            else:
                return c+1
        if num1==1:
            return c+num1
        else:return c+num1