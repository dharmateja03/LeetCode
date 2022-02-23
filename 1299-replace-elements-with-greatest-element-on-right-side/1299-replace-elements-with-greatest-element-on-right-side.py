class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=[-1]
        arr=arr[::-1]
        ans=arr[0]
        for i in arr:
            if i>ans:
                ans=i
            l.append(ans)
        return l[::-1][1:]
        
        
        