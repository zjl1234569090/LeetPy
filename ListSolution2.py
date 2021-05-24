#!/usr/bin/env python
# -*- encoding=utf-8 -*-

class ListNode:
    """
     链表节点
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_duplicates_v1(head: ListNode):
    """
    给的一个排序链表, 删除所有重复元素, 使得每个元素只出现一次.
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

def delete_duplicates_v2(head: ListNode):
    """
    给的一个排序链表, 只保留不重复出现的数字
    """
    if not head:
        return head

    dummy_node = ListNode(0)
    dummy_node.next = head
    head = dummy_node

    while head.next is not None and head.next.next is not None:
        if head.next.val = head.next.next.val:
            rm_val = head.next.val
            while head.next is not None and head.next.val == rm_val:
                head.next = head.next.next
        else:
            head = head.next
    return dummy_node.next

def reverse_list(head:ListNode):
    """
    翻转链表.
    """
    pre = None
    while head is not None:
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre


def reverse_between(head:ListNode):
    """
    翻转从位置 m 到 n 的链表, 请使用一趟扫描完成
    """
    if not head:
        return head
    dummy_node = None
    dummy_node.next = head
    head = dummy_node

    # 找到翻转部分的前一个节点
    pre = None

    for _ in range(m):
        pre = head
        head = head.next

    to_tail = head

    _pre = None
    for _ in range(n - m + 1):
        tmp = head.next
        head.next = _pre
        _pre = head
        head = tmp

    to_tail.next = head
    pre.next = _pre
    return dummy_node.next


def find_middle(head:ListNode):
    """
    寻找中间节点
    """
    if not head:
        return head

    slow = head
    fast = head.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

def merge_two_sorted_list(list_a:ListNode, list_b:ListNode):
    dummy_node = ListNode(0)
    head = dummy_node
    while list_a is not None and list_b is not None:
        if list_a.val <= list_b.val:
            head.next = list_a
            list_a = list_a.next
        else:
            head.next = list_b
            list_b = list_b.next
        head = head.next

    if list_a is not None:
        head.next = list_a
    if list_b is not None:
        head.next = list_b
    return dummy_node.next

def merge_sort(head:ListNode):
    if not head:
        return head
    mid = find_middle(head)
    second_part = mid.next
    mid.next = None
    first_part = head
    left = merge_sort(first_part)
    right = merge_sort(second_part)

    return merge_two_sorted_list(left, right)

def reorder_list(head:ListNode):
    if head is None:
        return head
    mid = find_middle(head)
    tail = reverse_list(mid.next)
    mid.next = None
    return merge_two_sorted_list(head, tail)
