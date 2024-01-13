class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        new_s = ''
        symbol = ''
        
        for l in s:
            if l.isdigit():
                new_s += l
            elif l in ('-', '+'):
                if new_s or symbol:
                    break
                symbol = l
            else:
                break
        
        if new_s:
            try:
                num = int(new_s)
                if symbol == '-':
                    num = -num
                return min(max(num, -2**31), 2**31-1)
            except ValueError:
                return 0
        else:
            return 0


    
obj = Solution()
print(obj.myAtoi("42"))
print(obj.myAtoi("    -42"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("00000-42a1234")) #0
print(obj.myAtoi("words and 987")) #0
print(obj.myAtoi("-91283472332")) #-2147483648
print(obj.myAtoi("+-2")) #0