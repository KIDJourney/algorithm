# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None :
            return 0

        nodequeue = [(root,1)]
        while nodequeue :
            node , count = nodequeue[0]
            del nodequeue[0]

            if node.left is not None :
                nodequeue.append((node.left,count+1))
            if node.right is not None:
                nodequeue.append((node.right,count+1))
            if not node.left and not node.righ :
                return count
        