class Solution:
    def letterCombinations(self, digits: str) :

        if len(digits)==0:
            return[]
        
        phoneNumSet={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        numToLet=[]
        def numToLetter(combo,nextDigits):
            if not nextDigits:
                numToLet.append(combo)
                return
            
            for letter in phoneNumSet[nextDigits[0]]:
                numToLetter(combo+letter,nextDigits[1:])

        numToLetter("",digits)
        return numToLet



obj = Solution()
print(obj.letterCombinations('23'))