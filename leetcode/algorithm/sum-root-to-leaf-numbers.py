class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.num_strings = []
        if root :
            self.visit(root, '')
        return sum(map(int, self.num_strings))

    def visit(self, node, strings):
        strings = strings + str(node.val)
        if node.left is None and node.right is None :
            self.num_strings.append(strings)
            return

        if node.left:
            self.visit(node.left, strings)
        if node.right:
            self.visit(node.right, strings)        

s = Solution()
tree_root = None

print(s.sumNumbers(tree_root))