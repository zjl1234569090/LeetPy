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

    def merge_two_lists(self, l1: ListNode, l2: ListNode):
        """
        将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
        :param l1:
        :param l2:
        :return:
        """
        dummy = ListNode(0)
        head = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        while l1 is not None:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2 is not None:
            head.next = l2
            l2 = l2.next
            head = head.next
        return dummy.next

    def partition_list(self, head: ListNode, x: int):
        """
        给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于  x  的节点都在大于或等于  x  的节点之前。
        :param head:
        :param x:
        :return:
        """
        if head is None:
            return None
        head_dummy = ListNode(0)
        head_dummy.next = head
        tail_dummy = ListNode(0)
        tail = tail_dummy
        head = head_dummy
        while head.next is not None:
            if head.next.val < x:
                head = head.next
            else:
                tmp = head.next
                head.next = head.next.next
                tail.next = tmp
                tail = tail.next

        tail.next = None
        head.next = tail_dummy.next
        return head_dummy.next

    def sort_list(self, head: ListNode):
        """
        在  O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
        思路：归并排序，找中点和合并操作
        :param head:
        :return:
        """
        return self.merge_sort(head)

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

    def merge_sort(self, head: ListNode):
        """
        归并排序
        :param head:
        :return:
        """
        if head is None or head.next is None:  # 递归返回的条件
            return head
        # 找到中间节点 断开
        middle = self.find_middle(head)
        tail = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(tail)
        return self.merge_two_lists(left, right)

    def reorder_list(self, head: ListNode):
        """
        给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
        将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        链接：https://leetcode-cn.com/problems/reorder-list
        :param head:
        :return:
        """

        if head is None:
            return head
        mid = self.find_middle(head)
        tail = self.reverse_list(mid.next)
        mid.next = None
        head = self.merge_two_lists(head, tail)
        return head

    def has_cycle(self, head: ListNode):
        """

        :param head:
        :return:
        """
        if head is None:
            return False

        fast = head.next
        slow = head

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False

    def has_cycle_v2(self, head: ListNode):
        """
        给定一个链表，返回链表开始入环的第一个节点。  如果链表无环，则返回  null.
        :param head:
        :return:
        """
        if head is None:
            return head

        fast = head.next
        slow = head
        while fast is not None and fast.next is not None:
            if fast == slow:
                fast = head
                slow = slow.next
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
            fast = fast.next.next
            slow = slow.next
        return None

    def is_palindrome(self, head: ListNode):
        """
        请判断一个链表是否为回文链表
        :param head:
        :return:
        """
        if head is None:
            return head
        slow = head
        fast = head.next
        # 找到中间节点
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        tail = self.reverse_list(slow.next)

        # 断开中间节点
        slow.next = None
        while head is not None and tail is not None:
            if head.val != slow.val:
                return False
            head = head.next
            tail = tail.next

        return True


