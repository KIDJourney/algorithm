class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import time

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None :
            return []

        stack = [root]
        ans = []
        flag = 1
        while stack:
            temp = []
            print(stack)
            for _ in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if flag :
                ans.append(temp[::])
            else:
                ans.append(temp[::-1])
            flag = 1 - flag
        
        return ans
