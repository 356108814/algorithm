#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.s1(root, targetSum)

    def s1(self, node: TreeNode, targetSum: int) -> bool:
        if not node:
            return False
        if not node.left and not node.right:
            return targetSum - node.val == 0
        return self.s1(node.left, targetSum - node.val) or self.s1(node.right, targetSum - node.val)
# @lc code=end

