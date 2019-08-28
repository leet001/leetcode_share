#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 08:34
# @Author  : ck
"""
题目:<两两交换链表中的节点>
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

    示例:

    给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def add_node(self, tail: ListNode, p: ListNode, q: ListNode) -> ListNode:
        new_node1 = ListNode(p.val)
        new_node2 = ListNode(q.val)
        tail.next = new_node2
        tail = tail.next
        tail.next = new_node1
        tail = tail.next
        return tail

    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode(0)
        if not head:
            return result.next
        tail = result
        p = head
        q = p.next

        while p and q:
            tail = self.add_node(tail, p, q)
            if q: p = q.next
            if p: q = p.next
        if p:
            new_node = ListNode(p.val)
            tail.next = new_node
        return result.next


"""
    递归法
"""


class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        res = head.next
        head.next = self.swapPairs(head.next.next)
        res.next = head

        return res


if __name__ == "__main__":
    s = Solution()

    data = [1, 2, 3, 4]
    head = ListNode(data[0])
    p = head
    for e in data[1:]:
        node = ListNode(e)
        p.next = node
        p = p.next
    result = s.swapPairs(head)
    while result:
        print(result.val)
        result = result.next

