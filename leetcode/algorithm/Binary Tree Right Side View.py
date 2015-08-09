    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Author: kidjourney
    # @Date:   2015-05-15 16:37:58
    # @Last Modified by:   kidjourney
    # @Last Modified time: 2015-05-15 18:39:41
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        # @param {TreeNode} root
        # @return {integer[]}
        def rightSideView(self, root):
            if not root :
                return []
            self.anslist = [root.val]
            self.rdir = {}
            self.ldir = {}
            self.mrl(root.right,self.rdir,0)
            self.mrl(root.left,self.ldir,0)
            print (self.rdir)
            print (self.ldir)
            self.anslist += dict(list(self.ldir.items()) + list(self.rdir.items())).values()
            return self.anslist

        def mrl(self,node,ndir,deep) :
            if node :
                ndir.setdefault(deep,node.val)
            else :
                return 
            self.mrl(node.right,ndir,deep+1)
            self.mrl(node.left,ndir,deep+1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)

job = Solution()
print(job.rightSideView(root))