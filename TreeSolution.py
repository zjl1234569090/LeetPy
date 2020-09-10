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
    @staticmethod
    def preorder_traversal(root: TreeNode) -> [int]:
        """
        前序非递归遍历
        :param root:
        :return:
        """
        result = []
        if root is None:
            return result
        s = [root]
        while len(s) > 0:
            node = s.pop()
            result.append(node.val)
            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)
        return result

    @staticmethod
    def inorder_traversal(root: TreeNode):
        """
        中序遍历
        :param root:
        :return:
        """
        s, result = [], []
        node = root
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                result.append(node.val)
                node = node.right
        return result

    @staticmethod
    def postorder_traversal(root: TreeNode):
        s, result = [], []
        node, last_visit = root, None
        while len(s) > 0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                node = s[-1]
                if node.right is not None and last_visit != node.right:
                    node = node.right
                else:
                    last_visit = s.pop()
                    result.append(last_visit.val)
        return result

    @staticmethod
    def level_order(root: TreeNode):
        """

        :param root:
        :return:
        """
        levels = []
        if root is None:
            return levels
        bfs = collections.deque([root])

        while len(bfs) > 0:
            levels.append([])
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                levels[-1].append(node.val)

                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        return levels

    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

    def is_balanced(self, root: TreeNode) -> bool:
        def depth(root):
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
