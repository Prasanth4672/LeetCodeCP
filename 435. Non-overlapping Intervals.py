class Solution:
    def eraseOverlapIntervals(self, intervals):
        slist=sorted(intervals, key=lambda x: x[1])
        count=1
        pos=slist[0][1]
        for key,val in enumerate(slist,start=1):
            if val[0] >= pos :
                pos=val[1]
                count+=1
            else:
                continue
        return len(slist)-count



obj = Solution()
"""print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(obj.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(obj.eraseOverlapIntervals([[1,2],[2,3]]))"""
print(obj.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))