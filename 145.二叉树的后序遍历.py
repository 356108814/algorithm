#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            res.append(node.val)

        res = []
        if not root:
            return res
        dfs(root)
        return res
# @lc code=end

