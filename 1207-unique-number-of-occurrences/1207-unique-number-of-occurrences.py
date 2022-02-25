class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[]
        for i in set(arr):
            l.append(arr.count(i))
        return len(l)==len(set(l))
        