class Solution:
    def countPoints(self, r: str) -> int:
        l=[[], [], [], [], [], [], [], [], [],[],[]]
        c=0
        for i in range(0,len(r)-1,2):
            l[int(r[i+1])].append(r[i])
        for i in l:
            if len(set(i))==3:
                c+=1
        return c
            
        