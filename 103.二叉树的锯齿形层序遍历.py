#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.solution2(root)

    def solution1(self, root: TreeNode) -> List[List[int]]:
        """
        思路：先得到层序遍历的结果，再对结果里的元素隔一反转
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            tmp = []
            res.append(tmp)
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        for x in range(len(res)):
            if x % 2 == 1:
                res[x].reverse()

        return res

    def solution2(self, root: TreeNode) -> List[List[int]]:
        """正常层序遍历，按层的遍历方向再特殊处理"""
        if not root:
            return []
        res = []
        q = [root]
        is_order_left = True
        while q:
            tmp = []
            res.append(tmp)
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if is_order_left:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            is_order_left = not is_order_left
        return res

# @lc code=end

