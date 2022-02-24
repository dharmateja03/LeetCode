class Solution:
    def canBeTypedWords(self, t: str, b: str) -> int:
        t=t.split()
        l=len(t)
        for i in t:
            for j in i:
                if j in set(b):
                    l-=1
                    break
        return l
                
        
        