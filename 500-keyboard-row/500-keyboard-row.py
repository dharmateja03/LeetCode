class Solution:
    def findWords(self, w: List[str]) -> List[str]:
        l=[]
        l1="qwertyuiop"
        l2="asdfghjkl"
        l3="zxcvbnm"
        c=0
        for i in w:
            if i[0] in l1 or i[0].swapcase() in l1:
                c=0
                while( c <len(i) and (i[c] in l1  or i[c].swapcase() in l1) ):
                    c+=1
                if c==len(i):
                    l.append(i)
            elif i[0] in l2 or i[0].swapcase() in l2:
                c=0
                while( c <len(i) and (i[c] in l2  or i[c].swapcase() in l2) ):
                    c+=1
                if c==len(i):
                    l.append(i)
            elif i[0] in l3 or i[0].swapcase() in l3:
                c=0
                while( c <len(i) and(i[c] in l3  or i[c].swapcase() in l3) ):
                    c+=1
                if c==len(i):
                    l.append(i)
        return l
       
        
        