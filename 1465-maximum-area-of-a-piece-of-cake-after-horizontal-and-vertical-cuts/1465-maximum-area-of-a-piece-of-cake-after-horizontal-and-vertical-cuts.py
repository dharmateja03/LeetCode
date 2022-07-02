class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
    # 11 13   
        hc=[0]+hc+[h]
        vc=[0]+vc+[w]
        #print(hc,vc)
        hamx,vmax=0,0
        m=pow(10,9)+7
        hc,vc=sorted(hc),sorted(vc)
        for i in range(1,len(hc)):
            
            hamx= max(hamx,hc[i]-hc[i-1])
                #print((hc[i]-hc[i-1])*(vc[j]-vc[j-1]), i ,j)
        for j in range(1,len(vc)):
            
            vmax= max(vmax,vc[j]-vc[j-1])
        #print(hamx,vmax,hc,vc)
        
        return (hamx*vmax)%m
            
        