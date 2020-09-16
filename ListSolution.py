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

    def delete_duplicates_v2(self, head: ListNode):
        """
        给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中   没有重复出现的数字。
        :param head:
        :return:
        """

        if head is None:
            return head
        # 链表头结点可能被删除，所以用 dummy node 辅助删除
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        while head.next is not None and head.next.next is not None:
            if head.next.val == head.next.next.val:
                # 记录已经删除的值 用于后续判断
                rm_val = head.next.val
                while head.next is not None and head.next.val == rm_val:
                    head.next = head.next.next
            else:
                head = head.next

        return dummy.next

    def reverse_list(self, head: ListNode):
        """
        翻转链表.
        :param head:
        :return:
        """
        pre = ListNode(0)
        while head is not None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre


    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        反转从位置  m  到  n  的链表。请使用一趟扫描完成反转。
        :param head:
        :param m:
        :param n:
        :return:
        """

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
