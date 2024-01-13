class Solution:
    def longestCommonPrefix(self, strs) -> str:
        sword=min(strs,key=len)
        for word in strs:
            while not word.startswith(sword):
                sword=sword[:-1]
        return sword



obj = Solution()
'''print(obj.longestCommonPrefix(["flower","flow","flcaaa"]))'''
print(obj.longestCommonPrefix(["caterpiller","racecar","car"]))