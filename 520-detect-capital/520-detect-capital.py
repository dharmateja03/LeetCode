class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        true,false=1,0
        if len(w)==1:
            return 1
        elif w[0].isupper() and w[1].isupper():
            for i in w:
                if not i.isupper():
                    return false
            return true
        elif w[0].isupper() and w[1].islower():
            for i in w[1:]:
                if not i.islower():
                    return false
            return true
        else:
            
            for i in w:
                if not i.islower():
                    return false
            return true
        
        