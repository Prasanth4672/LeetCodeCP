class Solution:
    def reverse(self, x: int) -> int:
        intMax = 2 ** 31 - 1
        intMin = -1 * 2 ** 31
        xStr = str(x) if x >= 0 else str(x)[1:]
        xRev = xStr[::-1] if x >= 0 else '-' + xStr[::-1]
        xRevInt = int(xRev)
        if xRevInt > intMax or xRevInt < intMin:
            return 0
        return xRevInt
    
obj= Solution()
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
print(obj.reverse(1534236469))