# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def find_sum(node, current_sum):
            if all([current_sum == targetSum, node.left == None, node.right == None]):
                return True
            if node.left:
                v = find_sum(node.left, current_sum + node.left.val)
                if v:
                    return True
            if node. right:
                return find_sum(node.right, current_sum + node.right.val)
            return False
        
        return find_sum(root, root.val)
        