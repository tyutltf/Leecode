# -*- encoding: utf-8 -*-
'''
@File    :   404-左叶子之和.py
@Time    :   2021/06/16 10:00:16
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''

计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        def DFS(root):
            if not root:
                return 0
            # 如果是左子树为左叶子节点，答案为左叶子数值加上右子树答案
            if root.left and not root.left.left and not root.left.right:
                return DFS(root.right) + root.left.val
            # 否则，答案为左右子树答案之和
            return DFS(root.left) + DFS(root.right)
        return DFS(root)
