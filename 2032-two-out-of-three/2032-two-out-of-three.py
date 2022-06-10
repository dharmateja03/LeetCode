class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d1={}
        d2={}
        d3={}
        l=set()
        ans=[]
        for i in set(nums1):
            l.add(i)
            d1[i]=d1.get(i,0)+1
        for i in set(nums2):
            l.add(i)
            d1[i]=d1.get(i,0)+1
        for i in set(nums3):
            l.add(i)
            d1[i]=d1.get(i,0)+1
        for i in d1:
            if d1[i]>1:
                ans.append(i)
        return ans