class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        def gd(s):
            s=set(s)
            for i in s :
                if (i.lower() in s )!=(i.upper() in s):
                    return False
            return True
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if gd(s[i:j]) and j-i>len(ans):
                    ans=s[i:j]
        return ans
        
        