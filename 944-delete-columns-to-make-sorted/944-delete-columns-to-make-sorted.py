class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        ans=0
        for i in range(len(s[0])):
            o=[]
            for j in s:
                o.append(j[i])
            if o!=sorted(o):ans+=1
        return ans   