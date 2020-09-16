#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: TreeNode.py
@Created: 2020/9/10 10:14 上午
@Contact: jiulinzeng@tencent.com
@Description: Definition for a binary tree node.

"""


class TreeNode:
    """
    二叉树的节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    """
    链表的节点

    链表相关的核心点
        null/nil 异常处理
        dummy node 哑巴节点
        快慢指针
        插入一个节点到排序链表
        从一个链表中移除一个节点
        翻转链表
        合并两个链表
        找到链表的中间节点
    """
    def __init__(self, x):
        self.val = x
        self.next = None
