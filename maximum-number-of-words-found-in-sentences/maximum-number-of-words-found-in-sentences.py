class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        l=[]
        for i in s:
            l.append(len(i.split()))
        return max(l)
        