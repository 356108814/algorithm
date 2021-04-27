#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.s1(root)

    def s1(self, root: TreeNode) -> int:
        depth = 0
        if root:
            find = False
            q = [root]
            while q:
                depth += 1
                n = len(q)
                for i in range(n):
                    node = q.pop(0)
                    if not node.left and not node.right:
                        find = True
                        break
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if find:
                    break
        return depth

# @lc code=end
