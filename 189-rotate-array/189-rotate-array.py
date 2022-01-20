class Solution:
    def rotate(self, l: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n=[0]*len(l)
        k=k%len(l)
        for i in range(len(l)):
            n[(i+k)%len(l)]=l[i]
        for i in range(len(l)):
            l[i]=n[i]
        
        
        
            
        