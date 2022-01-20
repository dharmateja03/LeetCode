class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        low=0
        h=len(nums)-1
        idx=h
        while(low<=h):
            if abs(nums[h])>=abs(nums[low]):
                l[idx]=nums[h]*nums[h]
                h-=1
            else:
                l[idx]=nums[low]*nums[low]
                low+=1
            idx-=1
        return l
                
            
        
            
        
        
        