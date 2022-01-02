class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:
        l=0
        h=len(nums)-1
        #m=l+h//2
        while(l<=h):
            m=(l+h) //2
            if nums[m]==t:
                return m
            elif nums[m]<t:
                l=m+1
            elif nums[m]>t:
                h=m-1
        return l
            

        