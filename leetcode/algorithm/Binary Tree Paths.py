# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path = []
        self.trave(root , [])
        print(self.path)
        self.path = ['->'.join([ j for j in i ]) for i in self.path]
        return self.path

    def trave(self , node , path):
        if (not node) :
            return
        path.append(str(node.val))
        if (not node.left and not node.right) :
            self.path.append(path)
            return

        if (node.left) :
            self.trave(node.left , path[:])
        if (node.right) :
            self.trave(node.right , path[:])

