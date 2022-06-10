class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        ans=[]
        for i in set(nums1):
            d1[i]=1
        for i in set(nums2):
            if i in d1:
                d1[i]+=1
        for i in d1:
            if d1[i]==2:
                ans.append(i)
        return ans