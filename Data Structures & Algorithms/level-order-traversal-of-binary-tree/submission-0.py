# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        level = 0
        ans = []
        
        def height(node):
            if node is None:
                return -1
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            return 1 + max(left_height, right_height)
            
        n = height(root)
        for _ in range(n + 1):
            ans.append([])

    
        def traverse(node, level):
            if not node:
                return
            
            ans[level].append(node.val)
            
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse(root, level)
     

        return ans
       