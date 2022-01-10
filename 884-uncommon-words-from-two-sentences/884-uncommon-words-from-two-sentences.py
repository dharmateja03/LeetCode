class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        l=[]
        for i in s1.split():
            d[i]=d.get(i,0)+1
        for i in s2.split():
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==1:
                l.append(i)
        return l
        