class Solution:
    def generate(self, num: int) -> List[List[int]]:
        ans=[[1]*(i+1) for i in range(num)]
        for i in range(num):
            for j in range(1,i):
                ans[i][j]=ans[i-1][j]+ans[i-1][j-1]
        return ans
       
            
            
            
            
        