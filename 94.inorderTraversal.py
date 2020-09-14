# coding: utf-8
# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序遍历。

# 示例:

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
            print(root.val)

        return self.res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.inorderTraversal(root))