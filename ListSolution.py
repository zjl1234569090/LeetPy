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
    def delete_duplicates(self, head: ListNode) -> ListNode:
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

