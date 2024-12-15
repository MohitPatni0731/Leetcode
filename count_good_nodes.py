# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [root]  
        max_values = [root.val]
        good_nodes = 0
        
        while stack:
            node = stack.pop()
            max_so_far = max_values.pop()
            if node.val >= max_so_far:
                good_nodes += 1
            
            new_max = max(max_so_far, node.val)
            
            if node.right:
                stack.append(node.right)
                max_values.append(new_max)
            if node.left:
                stack.append(node.left)
                max_values.append(new_max)
        
        return good_nodes
