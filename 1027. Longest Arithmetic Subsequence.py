class Solution:
    def longestArithSeqLength(self, nums) -> int:
        dp ={}
        n = len(nums)
        if n <= 2:
            return n
        for r in range(n):
            for l in range(r):
                diff = nums[r] -nums[l]
                dp[(r,diff)] = dp.get((l,diff),1)+1
        return max(dp.values())

obj = Solution()    
print(obj.longestArithSeqLength([20,1,15,3,10,5,8]))