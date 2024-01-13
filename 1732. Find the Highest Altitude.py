class Solution:
    def largestAltitude(self, gain) -> int:
        carry = 0
        result = carry
        for n in gain:
            carry += n
            result=max(result, carry)
        return result


obj = Solution()
print(obj.largestAltitude([44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]))
print(obj.largestAltitude([-4,-3,-2,-1,4,3,2]))
print(obj.largestAltitude([-5,1,5,0,-7]))