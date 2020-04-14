# coding: utf-8
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#  
# 进阶：
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#  
# 示例：
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = self.listNodeToNumber(l1)
        v2 = self.listNodeToNumber(l2)
        v = v1 + v2

        result = None
        p = None
        sumStr = str(v)
        for i in range(len(sumStr)):
            val = int(sumStr[i])
            if not result:
                result = ListNode(val)
                p = result
            else:
                p.next = ListNode(val)
                p = p.next
        return result

    def listNodeToNumber(self, l: ListNode):
        s = ''
        p = l
        while p:
            s += str(p.val)
            p = p.next

        return int(s)


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = self.listNodeToStack(l1)
        s2 = self.listNodeToStack(l2)

        result = None
        carry = 0
        while s1 or s2 or carry != 0:
            v1 = 0 if not s1 else s1.pop()
            v2 = 0 if not s2 else s2.pop()
            cur =  v1 + v2 + carry
            carry = cur // 10
            cur %= 10
            curNode = ListNode(cur)
            curNode.next = result
            result = curNode
        return result

    def listNodeToStack(self, l: ListNode):
        stack = []
        p = l
        while p:
            stack.append(p.val)
            p = p.next
        return stack