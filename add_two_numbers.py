# -*- coding: utf-8 -*-
"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        flag = 0
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + flag) % 10)
            flag = (l1.val + l2.val + flag) / 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val + flag) % 10)
                flag = (l2.val + flag) / 10
                l2 = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val + flag) % 10)
                flag = (l1.val + flag) / 10
                l1 = l1.next
                p = p.next
        if flag == 1:
            p.next = ListNode(1)
        return dummy.next
