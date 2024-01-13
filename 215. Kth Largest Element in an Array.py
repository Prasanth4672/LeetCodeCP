import heapq as hq
class Solution:
    def findKthLargest(self, nums:list[int], k: int) -> int:
        heap = [nums[i] for i in range(k)]
        hq.heapify(heap)
        for i in range(k,len(nums)):
            if nums[i] > heap[0]:
                hq.heappushpop(heap, nums[i])
        return heap[0]

        




obj = Solution()
print(obj.findKthLargest([3,2,1,5,6,4],2))
print(obj.findKthLargest([3,2,3,1,2,4,5,5,6],4))
        