class Solution:
    def isValid(self, s: str) -> bool:
        resstack=[]
        sdict={')':'(','}':'{',']':'['}
        for char in s:
            if char in sdict.values():
                resstack.append(char)
            elif char in sdict.keys():
                if not resstack or sdict[char]!=resstack.pop():
                    return False
            else:
                return False
        
        return not resstack
    

obj = Solution()
print(obj.isValid('()'))