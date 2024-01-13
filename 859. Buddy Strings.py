class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
           return len(set(s)) < len(goal) 
        
        findex = -1
        sindex = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if findex == -1:
                    findex = i
                elif sindex == -1:
                    sindex = i
                else:
                    return False
        if sindex == -1:
            return False
        return s[findex] == goal[sindex] and s[sindex] == goal[findex]
    



obj = Solution()
print(obj.buddyStrings("ab","ab"))
print(obj.buddyStrings("ab","ba"))
print(obj.buddyStrings("aa","aa"))
