#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:06
# @Author  : ck
"""
题目:<合并两个有序链表>
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def common(self, l: ListNode, p: ListNode) -> ListNode:
        p.next = l
        l = l.next
        p = p.next
        return l, p

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head

        while l1 and l2:
            if l1.val == l2.val:
                l1, p = self.common(l1, p)
                l2, p = self.common(l2, p)
            elif l1.val <= l2.val:
                l1, p = self.common(l1, p)
            elif l1.val >= l2.val:
                l2, p = self.common(l2, p)

        if l1:
            while l1:
                l1, p = self.common(l1, p)
        elif l2:
            while l2:
                l2, p = self.common(l2, p)
        return head.next


if __name__ == "__main__":

    s = Solution()
    l1 = None
    l2 = ListNode(0)
    result = s.mergeTwoLists(l1, l2)

    while result:
        print(result.val)
        result = result.next


"""
官方题解，递归法
说明:
    备注： 在 Python 中，and 和 or 都有提前截至运算的功能。
    
    and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
    or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
    例子：[] and 7 等于 []
    代码流程：（按行数）
    
    判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
    对 l1 和 l2 重新赋值，使得 l1 指向比较小的那个节点对象
    修改 l1 的 next 属性为递归函数返回值
    返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None
"""


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2




