# coding: utf-8

# 反转单链表
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
