#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 10:25
# @Author  : ck
"""
题目:<删除链表的倒数第N个节点>
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

    示例：

    给定一个链表: 1->2->3->4->5, 和 n = 2.

    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：

    给定的 n 保证是有效的。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
           :type head: ListNode
           :type n: int
           :rtype: ListNode
       """
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy
        for _ in range(n + 1):
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    data = [1, 2, 3, 4, 5]
    head = ListNode(data[0])
    # p = head
    # for i in data[1:]:
    #     node = ListNode(i)
    #     p.next = node
    #     p = p.next

    n = 1
    result = s.removeNthFromEnd(head, n)
    print(result)
    while result:
        print(result.val)
        result = result.next
