class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l,r=0,0
        ans=[]
        c=""
        for i in s:
            if i=="L":
                l+=1
            else:r+=1
            if l==r:
                ans.append(c)
                l,r=0,0
            else:
                c+=i
        return len(ans)
            
        