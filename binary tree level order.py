# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1475064404/

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
        
        stk = [root]
        level_order = []
        
        while stk:
            level = []
            
            for _ in range(len(stk)):
                node = stk.pop(0)
                level.append(node.val)
                
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
            
            level_order.append(level)
        
        return level_order
