class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        d2={}
        ans=[]
        for i in nums1:
            d1[i]=d1.get(i,0)+1
        for i in nums2:
            d2[i]=d2.get(i,0)+1
        for i in d1:
            if i in d2:
                ans=ans+ min(d1[i],d2[i])*[i]
        return ans
        
        