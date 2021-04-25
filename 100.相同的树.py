#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.s1(p, q)

    def s1(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归判断，关键要注意节点都没有的情况
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.s1(p.left, q.left) and self.s1(p.right, q.right)
        else:
            return False

    def s2(self, p: TreeNode, q: TreeNode) -> bool:
        pass

# @lc code=end

