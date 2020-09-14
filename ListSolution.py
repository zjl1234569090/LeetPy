#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: ListSolution.py
@Created: 2020/9/10 2:30 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""

from StructCollections import ListNode


class Solution:
    def delete_duplicates(self, head: ListNode):
        """
        给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
        :param head:
        :return:
        """
        if head is None:
            return head

        current = head

        while current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    def delete_duplicates_v2(self, head: ListNode) -> ListNode:
        """
        给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中   没有重复出现的数字。
        :param head:
        :return:
        """

        if head is None:
            return head
        dummy = ListNode()
        dummy.next = head

        current, peek = dummy, head
        find_dup = False
        while peek.next is not None:
            if peek.next.val == peek.val:
                find_dup = True
                peek.next = peek.next.next
            else:
                if find_dup:
                    find_dup = False
                    current.next = current.next.next
                else:
                    current = current.next
                peek = peek.next

        if find_dup:
            current.next = current.next.next

        return dummy.next

    def reverse_list(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        tail = head
        while tail.next is not None:
            # put tail.next to head
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = head
            head = tmp

        return head

    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        反转从位置  m  到  n  的链表。请使用一趟扫描完成反转。
        :param head:
        :param m:
        :param n:
        :return:
        """

        """ 循环迭代 -- 找到前一个节点，反转，重新链接 """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 1: 找到反转部分的前一个节点
        for _ in range(m - 1):
            pre = pre.next

        # 2: 反转链表
        node = pre  # 记录前继节点
        cur = pre.next
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next  # 此处的交换方法记住

        # 3: 将反转后的子链表，拼接回原链表
        node.next.next = cur
        node.next = pre

        return dummy.next
