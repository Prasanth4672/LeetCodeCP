class Solution:
    def twoSum(self, nums, target: int) :
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []


obj = Solution()
print(obj.twoSum([2,7,11,15],9))
print(obj.twoSum([3,2,4],6))