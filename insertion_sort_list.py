"""
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。



插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy

        while cur is not None:
            lat = cur.next
            if lat is not None and lat.val < cur.val:
                while pre.next is not None and pre.val < lat.val:
                    pre = pre.next
                temp = pre.next
                pre.next = lat
                cur.next = lat.next
                lat.next = temp.next
                pre = dummy
            else:
                cur = lat

        return dummy.next

    def printNode(node):
        while node is not None:
            print(node.val)
            node = node.next


if __name__ == "__main__":

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    s = Solution()

    ret = s.insertionSortList(head)

    while ret is not None:
        print(ret.val)
        ret = ret.next
