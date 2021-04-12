#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """平衡二叉树：空树 或者 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 """

    def isBalanced(self, root: TreeNode) -> bool:
        return self.solution2(root)

    def solution1(self, root: TreeNode) -> bool:
        """递归"""

        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            return max(left_height, right_height) + 1

        if not root:
            return True
        if self.solution1(root.left) and self.solution1(root.right) and abs(get_height(root.left) - get_height(root.right)) <= 1:
            return True
        return False

    def solution2(self, root: TreeNode) -> bool:
        """自底向上，不平衡返回高度为-1"""

        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1
        
        return get_height(root) >= 0


# @lc code=end
