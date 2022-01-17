class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        l1,l2=[],[]
        for i in s.split():
            l1.append(s.split().index(i))
        for i in list(p):
            l2.append(p.find(i))
        return l1==l2
            
            
        