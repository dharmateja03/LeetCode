class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        d={}
        for i in range(1,len(nums)+1):
            d[i]=0
        for i in nums:
            d[i]+=1
        for i in d:
            if d[i]==0:
                ans.append(i)
        return ans
        
        
        
        