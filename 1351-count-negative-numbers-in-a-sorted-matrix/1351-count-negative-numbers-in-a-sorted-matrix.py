class Solution:
    def countNegatives(self, g: List[List[int]]) -> int:
        c=0
        for i in g:
            for j in i:
                if j<0:
                    c+=1
        return c