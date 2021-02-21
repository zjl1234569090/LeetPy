#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import collections

class TreeNode:
    """
    二叉树
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_traversal(root:TreeNode):
    """
    前序遍历
    """
    result = []
    if root is None:
        return result

    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            result.append(root.val)  # 遍历根节点
            stack.append(root)
            root = root.left

        node = stack.pop()
        root  = node.right
    return result

def in_order_traversal(root:TreeNode):
    """
    中序遍历
    """
    result = []
    if root is None:
        return result
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            stack.append(root)
            root = root.left
        node = stack.pop()
        result.append(node.val)
        root = node.right
    return result

def post_order_traversal(root:TreeNode):
    """
    后续遍历
    """
    stack = []
    node, last_visit = root, None
    while node is not None or len(stack) > 0:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if node.right is not None and last_visit != node.right:
                node = node.right
            else:
                last_visit = stack.pop()
                result.append(last_visit.val)
    return result

def level_traversal(root:TreeNode):
    """
    层次遍历
    """
    results = []
    if root is None:
        return results
    bfs = collections.deque([root])
    while len(bfs) > 0:
        results.append([])
        level_size = len(bfs)
        for _ in range(level_size):  # 遍历层中的每一个节点
            node = bfs.popleft()
            results[-1].append(node.val)
            if node.left is not None:
                bfs.append(node.left)
            if node.right is not None:
                bfs.append(node.right)
    return results

