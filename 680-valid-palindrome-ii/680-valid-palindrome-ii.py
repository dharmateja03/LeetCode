class Solution:
    #aacbbaa
    def validPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        if s==s[::-1]:
            return True
        while(l<=h and h>0 and l<len(s)-1):
            if s[l]!=s[h]:
                s1=s[:l]+s[l+1:]
                s2=s[:h]+s[h+1:]
                return s1==s1[::-1] or s2==s2[::-1]
            l+=1
            h-=1
        return 1
        
        
            
            
            
        