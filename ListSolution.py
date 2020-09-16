#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: ListSolution.py
@Created: 2020/9/10 2:30 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""

from StructCollections import ListNode, pretty_print_linked_list


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
        pre = None
        while head is not None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
            # 上述 4 行代码, 在 python 下直接可以用下面一行替代
            # head.next, pre, head = pre, head, head.next
        return pre

    def reverse_between(self, head: ListNode, m: int, n: int):
        """
        反转从位置  m  到  n  的链表。请使用一趟扫描完成反转。
        :param head:
        :param m:
        :param n:
        :return:
        """
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        # 1: 找到反转部分的前一个节点
        pre = None
        for _ in range(m):
            pre = head
            head = head.next

        # 2: 反转链表
        mid = head  # 记录前继节点
        _pre = None
        for _ in range(n - m + 1):
            if head is None:
                break
            tmp = head.next
            head.next = _pre
            _pre = head
            head = tmp
            # 或者采用如下语句进行链表翻转
            # head.next, _pre, head = _pre, head, head.next


        # 3: 将反转后的子链表，拼接回原链表
        pre.next = _pre
        mid.next = head

        return dummy.next

    def sort_list(self, head:ListNode):
        """
        在  O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
        思路：归并排序，找中点和合并操作
        :param head:
        :return:
        """
        pass

    def find_middle(self, head):
        """
        找到链表中间的节点.
        :param head:
        :return:
        """
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow



