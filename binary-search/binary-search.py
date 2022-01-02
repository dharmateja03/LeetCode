class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l=0
        h=len(nums)-1
        m=int(l+h)//2
        while(l<=h):
            m=int(l+h)//2
            if nums[m]>t:
                h=m-1
            elif nums[m]<t:
                l=m+1
            else:return m
        return -1
        