#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversa(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return res


# @lc code=end

