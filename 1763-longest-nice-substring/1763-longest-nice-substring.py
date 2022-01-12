class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            for j in range(i):
                if set(s[j:i+1])==set(s[j:i+1].swapcase()):
                    ans=max(ans,s[j:i+1],key=len)
        return ans
        