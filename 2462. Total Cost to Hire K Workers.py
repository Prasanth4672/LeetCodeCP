from heapq import *

class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        head = costs[:candidates]
        tail = costs[max(candidates, len(costs) - candidates):]
        heapify(head)
        heapify(tail)
        
        res = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates 

        for _ in range(k): 
            if not tail or head and head[0] <= tail[0]: 
                res += heappop(head)

                if next_head <= next_tail: 
                    heappush(head, costs[next_head])
                    next_head += 1
            else: 
                res += heappop(tail)
                if next_head <= next_tail:  
                    heappush(tail, costs[next_tail])
                    next_tail -= 1
                    
        return res

obj = Solution()
print(obj.totalCost([17,12,10,2,7,2,11,20,8],3,4))