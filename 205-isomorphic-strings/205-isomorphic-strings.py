class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1,d2={},{}
        for i,q in enumerate(s):
            d1[q]=d1.get(q,[])+[i]
        for i,q in enumerate(t):
            d2[q]=d2.get(q,[])+[i]
        return sorted(d1.values())==sorted(d2.values())
        
        
        
        