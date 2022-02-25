class Solution:
    def groupThePeople(self, groupSizes):
        d, result = defaultdict(list), []
        for i,g in enumerate(groupSizes):
            dg = d[g]
            dg.append(i)
            if len(dg)==g:
                result.append( [*dg] )
                dg.clear()
        return result

        
        