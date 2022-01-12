class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        curr=1
        i=1
        ans=0
        while i<len(s):
            if s[i-1]==s[i]:
                curr+=1
            else:
                ans+=min(prev,curr)
                prev=curr
                curr=1
            i+=1
        ans+=min(prev,curr)
        return ans
        