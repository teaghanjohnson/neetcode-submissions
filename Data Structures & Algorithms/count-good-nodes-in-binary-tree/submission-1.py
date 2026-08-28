# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return

        num = root.val
        good_nodes = 0
        
        def dfs(node, maxVal):
            nonlocal num
            nonlocal good_nodes

            if node is None:
                return
            
            if node.val >= maxVal:
                good_nodes += 1
                dfs(node.left, maxVal = node.val)
                dfs(node.right, maxVal = node.val)
            
            else:
                dfs(node.left, maxVal)
                dfs(node.right, maxVal)

        dfs(root, maxVal = root.val)

        return good_nodes
            

            
            

            

