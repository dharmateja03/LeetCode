class Solution:
    def minOperations(self, b: str) -> List[int]:
        l=[]
        ans=[]
        for i in range(len(b)):
            if b[i]=="1":
                l.append(i)
        for i in range(len(b)):
            c=0
            for j in l:
                c+= abs(j-i)
            ans.append(c)
        return ans