class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l=min(len(w1),len(w2))
        s=""
        for i in range(l):
            s+=w1[i]+w2[i]
        if len(w1)>len(w2):
            s+=w1[i+1:]
        elif len(w1)<len(w2):
            s+=w2[i+1:]
        return s
        