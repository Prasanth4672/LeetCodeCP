class Solution:
    def removeDuplicates(self, nums) -> int:
        nums[:] = sorted(set(nums))
        return type(len(nums))



obj=Solution()
print(obj.removeDuplicates([1,1,2]))
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))