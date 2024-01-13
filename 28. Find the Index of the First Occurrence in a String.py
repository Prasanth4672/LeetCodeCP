class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        new = haystack.replace(needle,'A')
        if (new == haystack): return -1
        else: return new.index('A')
        
    

obj = Solution()
print(obj.strStr("sadbutsad","sad"))