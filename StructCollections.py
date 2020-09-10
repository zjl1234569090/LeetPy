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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
