# Definition for a binary tree node.
import collections


class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        max_sum,result,nodeLevel=float('-inf'),0,0
        
        que = collections.deque()
        que.append(root)

        while que :
            nodeLevel+=1
            temp_level_sum = 0

            for _ in range(len(que)):
                node = que.popleft()
                temp_level_sum+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            
            if max_sum < temp_level_sum :
                max_sum, result = temp_level_sum, nodeLevel
        return result
    

l7 = TreeNode(70)
l6 = TreeNode(50)
l5 = TreeNode(30)
l4 = TreeNode(10)
l3 = TreeNode(65)
l3.left = l6
l3.right = l7
l2 = TreeNode(25)
l2.left = l4
l2.right = l5
l1 = TreeNode(40)
l1.left = l2
l1.right = l3
 
obj = Solution()
print(obj.maxLevelSum(l1))

