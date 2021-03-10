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
        return self.postorderTraversal2(root)

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """迭代单栈写法"""
        res = []
        stack = []
        prev = None
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                # 当前访问的节点是叶子节点或当前访问的节点的右子节点是上一次访问的节点。
                res.append(node.val)
                prev = node
                node = None # 此处为了跳过下一次循环的访问左子节点的过程，直接进入栈的弹出阶段，因为但凡在栈中的节点，它们的左子节点都肯定被经过且已放入栈中。
            else:
                stack.append(node)
                node = node.right
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代双栈写法，由前序遍历变形，先根右左，再倒序即为左右根"""
        res = []
        tmp = []
        stack = []
        node = root
        while node or stack:
            while node:
                tmp.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        while tmp:
            res.append(tmp.pop())
        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode):
            if node:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                res.append(node.val)

        dfs(root)
        return res
# @lc code=end

