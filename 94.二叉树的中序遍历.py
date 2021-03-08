#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:

        def dfs(node: TreeNode, res: List[int]):
            if node.left:
                dfs(node.left, res)
            res.append(node.val)
            if node.right:
                dfs(node.right, res)
        
        if not root:
            return []

        res = []
        dfs(root, res)
        return res
# @lc code=end

