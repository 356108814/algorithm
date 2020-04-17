# coding: utf-8
# 19.
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(0, n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 给链表添加伪头节点
        dummy = ListNode(0)
        dummy.next = head
        # 计算链表长度
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
            
        # 删除第index个节点
        index = length - n
        p = dummy
        for _ in range(index):
            p = p.next
        p.next = p.next.next
        return dummy.next

