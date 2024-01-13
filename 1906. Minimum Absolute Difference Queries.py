from bisect import bisect_left
from cmath import inf
import sys


class Solution:
    def minDifference(self, nums, queries):
        sdict={}
        for key,val in enumerate(nums):
            if val in sdict:
                sdict[val].append(key)
            else:
                sdict[val]=[key]
        
        keys=sorted(sdict)
        res =[]
        for start,end in queries:
            prev,val=0,inf
            for key in keys:
                i=bisect_left(sdict[key],start)
                if i < len(sdict[key]) and sdict[key][i]<=end :
                    if prev:
                        val=min(val,key-prev)
                    prev=key
            if val<inf:
                res.append(val)
            else:
                res.append(-1)
        return res
          
        



obj = Solution()
print(obj.minDifference([1,3,4,8],[[0,1],[1,2],[2,3],[0,3]]))
print(obj.minDifference([4,5,2,2,7,10],[[2,3],[0,2],[0,5],[3,5]]))
print(obj.minDifference([7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],[[38,43],[35,36],[33,40],[5,21],[46,48],[31,49],[48,49],[44,48],[41,49],[28,29]]))
print(obj.minDifference([10,6,10,4,2],[[1,3],[0,2],[1,2],[2,3],[3,4]]))
