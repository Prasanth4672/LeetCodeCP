from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str):
        dict1=Counter(s)
        dict2=Counter(t)
        if len(dict1) != len(dict2):
            return False
    
        # Step 2: Compare keys
        if set(dict1.keys()) != set(dict2.keys()):
            return False
    
        # Step 3: Compare values
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False
    
        # Dictionaries are equal
        return True
    






obj= Solution()
print(obj.isAnagram("anagram", "nagaram"))
print(obj.isAnagram("rat", "car"))