# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_level = 0
        self.max_value = 0

        queue = [root]
        level = 0
        while queue:
            new_queue = []
            level_sum = 0
            for node in queue:
                if not node:
                    continue
                level_sum += node.val
                new_queue.append(node.left)
                new_queue.append(node.right)

            if level_sum > self.max_value:
                self.max_value = level_sum
                self.max_level = level

            queue = new_queue
            level += 1

        return self.max_level + 1
