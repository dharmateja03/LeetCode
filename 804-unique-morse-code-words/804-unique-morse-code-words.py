class Solution:
    def uniqueMorseRepresentations(self, w: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=[]
        d={}
        for i in w:
            e=""
            for j in range(len(i)):
                e+=l[ord(i[j])-ord("a")]
            ans.append(e)
        for u in ans:
            d[u]=d.get(u,0)+1
        return len(set(d.keys()))
                
        