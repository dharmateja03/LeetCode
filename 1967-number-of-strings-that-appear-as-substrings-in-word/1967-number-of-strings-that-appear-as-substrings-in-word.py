class Solution:
    def numOfStrings(self, p: List[str], w: str) -> int:
        c=0
        for i in p:
            if i in w:
                c+=1
                
        return c
            
       
        