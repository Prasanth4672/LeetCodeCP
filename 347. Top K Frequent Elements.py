from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        res=[]
        sdict={}
        for num in nums:
            if num in sdict.keys():
                sdict[num]+=1
            else:
                sdict[num]=1
        sort_dict = sorted(sdict.items(), key=lambda x: x[1], reverse=True)

        '''for i in sort_dict:
            if k <= 0:
                break
            res.append(i[0])
            k-=1'''
        return [val[0] for i,val in enumerate(sort_dict) if i < 2 ]
obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3],2))