class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        l=[]
        n=len(arr)
        for i in range(2**n):
            ans=[]
            for j in range(n):
                if i& 1<<j:
                    ans.append(arr[j])
            l.append(ans)
        return l
        