class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        ans=0
        for i in s:
            while i in d:
                d.remove(s[l])
                l+=1
            d.add(i)
            ans=max(ans,len(d))
        return ans
            
            
            
            
        