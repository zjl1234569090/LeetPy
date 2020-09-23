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



class MinStack:
    """
    栈的特点是后入先出
    """
    def __init__(self):
        self.stack = []

    def push(self, x):
        """

        :param x:
        :return:
        """
        if len(self.stack) > 0:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self):
        """

        :return:
        """
        return self.stack.pop()[0]

    def top(self):
        """

        :return:
        """
        return self.stack[-1][0]

    def get_min(self):
        """

        :return:
        """
        return self.stack[-1][1]

class Queue:
    def __init__(self):
        self.cache = []
        self.out = []

    def push(self, x: int):
        """

        :param x:
        :return:
        """
        self.cache.append(x)

    def pop(self):
        """

        :return:
        """
        if len(self.out) == 0:
            while len(self.cache) > 0:
                self.out.append(self.cache.pop())
        return self.out.pop()

    def peek(self):
        """

        :return:
        """
        if len(self.out) > 0:
            return self.out[-1]
        else:
            return self.cache[0]

    def empty(self):
        """

        :return:
        """
        return len(self.cache) == 0 and len(self.out) == 0



