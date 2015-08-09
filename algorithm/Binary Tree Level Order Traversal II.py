# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root :
            return []

        ans = []
        queue = [root]
        temp = []
        while 1 :
            temp = []
            ans.append([i.val for i in queue])
            for i in queue :
                if i.left :
                    temp.append(i.left)
                if i.right :
                    temp.append(i.right)
            
            if len(temp) == 0 :
                break
            queue = temp[:]
        return ans