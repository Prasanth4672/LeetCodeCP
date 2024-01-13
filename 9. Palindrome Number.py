class Solution:
    def isPalindrome(self, x: int) -> bool:
        res =0
        d=x
        while(d>0 & d%10 ):
            res=res*10+(d%10)
            d=d//10
        if(res==x):
            return True
        return False
    

obj= Solution()
print(obj.isPalindrome(-121))