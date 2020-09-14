#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: TreeSolution.py
@Created: 2020/9/10 10:16 上午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from StructCollections import TreeNode
import collections


class Solution:
    def __init__(self):
        self.result = []

    def pre_order_traversal(self, root: TreeNode) -> [int]:
        """
        前序非递归遍历
        :param root:
        :return:
        """
        if root is None:
            return self.result
        stack = []
        while root is not None or len(stack) > 0:
            while root is not None:
                self.result.append(root.val)
                stack.append(root)  # 存储已经遍历的节点, 用于后续回溯右节点
                root = root.left
            node = stack.pop()
            root = node.right
        return self.result

    def in_order_traversal(self, root: TreeNode):
        """
        中序遍历
        :param root:
        :return:
        """
        stack = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            node = stack.pop()
            self.result.append(node.val)
            root = root.right
        return self.result

    def post_order_traversal(self, root: TreeNode):
        stack = []
        node, last_visit = root, None
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right is not None and last_visit != node.right:
                    node = node.right
                else:
                    last_visit = stack.pop()
                    self.result.append(last_visit.val)
        return self.result

    def level_order(self, root: TreeNode):
        """
        层次遍历
        :param root:
        :return:
        """
        if root is None:
            return self.result
        bfs = collections.deque([root])
        while len(bfs) > 0:
            self.result.append([])
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                self.result[-1].append(node.val)

                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        return self.result

    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

    def is_balanced(self, root: TreeNode) -> bool:
        def depth(root:TreeNode):
            if root is None:
                return 0, True

            dl, bl = depth(root.left)
            dr, br = depth(root.right)

            return max(dl, dr) + 1, bl and br and abs(dl - dr) < 2

        _, out = depth(root)
        return out

    @staticmethod
    def max_path_sum(root: TreeNode):
        max_path = float('-inf')
        if root is None:
            return float('-inf')
        e_l = Solution.max_path_sum(root.left)
        e_r = Solution.max_path_sum(root.right)
        max_path = max(max_path, root.val + max(0, e_l) + max(0, e_r), e_l, e_r)
        return max_path

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None

    def insert_into_bst(self, root: TreeNode, val: int) -> TreeNode:

        if root is None:
            return TreeNode(val)

        node = root
        while True:  # keep trying until finding the right position
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
