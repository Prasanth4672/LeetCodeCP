class Solution:
    def longestSubarray(self, nums) -> int:

        zeroCount = 0;
        longestWindow = 0;
        start = 0;
        
        for i in range(len(nums)):
            zeroCount += 1 if nums[i] == 0 else 0
            while (zeroCount > 1) :
                zeroCount -= 1 if nums[start] == 0 else 0
                start+=1
            longestWindow = max(longestWindow, i - start)
    
        return longestWindow;

    


obj = Solution()
print(obj.longestSubarray([1,1,0,1]))
print(obj.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(obj.longestSubarray([1,1,1]))