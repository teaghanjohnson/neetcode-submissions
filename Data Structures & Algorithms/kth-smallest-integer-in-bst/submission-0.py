# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        count = 0
        def levelOrder(node):
            nonlocal count, ans
            # Base case
            if not node or ans is not None:
                return

            levelOrder(node.left)

            count += 1
            if count == k:
                ans = node.val
                return

            levelOrder(node.right)

        levelOrder(root)
        return ans
      
        
        


                    
        
        


                    

        