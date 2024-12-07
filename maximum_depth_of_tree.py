# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = []
        queue.append(root)
        
        while queue:
            level = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level += 1

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
        return level + 1
