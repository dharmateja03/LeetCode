class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls,lt=0,0
        for i in t:
            if ls<len(s) and i==s[ls]:
                ls+=1
        return ls==len(s)