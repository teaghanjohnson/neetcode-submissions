# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse through root until val = subroot.val
        # continue traversal but of both trees if they dont match return False
        # else return True
        if root is None:
            return False

            
        def same_tree(root, subRoot):

            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if root.val != subRoot.val:
                return False

            return same_tree(root.left, subRoot.left) and same_tree(root.right, subRoot.right)


        if same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)