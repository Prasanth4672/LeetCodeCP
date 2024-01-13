class Solution:
    def longestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        temp=''
        result =[]
        for c in s:
            if temp in rev:
                temp +=c
            else:
                result.append(temp)
                temp= temp[1:]
        return max(result)


obj =Solution()
print(obj.longestPalindrome('babad'))
print(obj.longestPalindrome('cbbd'))