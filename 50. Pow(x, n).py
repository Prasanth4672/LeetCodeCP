class Solution:
    def myPow(self, x: float, n: int) -> float: 
        if n==0 :
            return 1 
        if n < 0:
            x = 1 / x
            n = abs(n)
        
        result = self.myPow(x,n//2)
        if n%2 == 0:
            result =  result * result
        else:
            result = x * result * result 
        return round(result,5)
    
obj = Solution()
print(obj.myPow(2.10000,3))
print(obj.myPow(2.00000,-2))