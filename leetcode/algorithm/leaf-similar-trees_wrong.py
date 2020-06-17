class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.find_leaf(root1) == self.find_leaf(root2)

    @staticmethod
    def find_leaf(node):
        ret = []
        queue = [node]
        new_queue = []
        while queue:
            for n in queue:
                if n is None:
                    continue

                is_leaf = True

                if n.left:
                    new_queue.append(n.left)
                    is_leaf = False
                if n.right:
                    new_queue.append(n.right)
                    is_leaf = False

                if is_leaf:
                    ret.append(n.val)
            queue, new_queue = new_queue, []

        return ret


s = Solution()
print(s.find_leaf(TreeNode(1)))
