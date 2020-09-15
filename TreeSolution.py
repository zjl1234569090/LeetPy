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
        if root is None:
            return True
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return self.is_balanced(root.left) and self.is_balanced(
            root.right) and abs(left_depth - right_depth) <= 1

    def max_path_sum(self, root: TreeNode):
        """
        给定一个非空二叉树，返回其最大路径和.
        思路：分治法，分为三种情况：左子树最大路径和最大，右子树最大路径和最大，
        左右子树最大加根节点最大，需要保存两个变量：一个保存子树最大路径和，
        一个保存左右加根节点和，然后比较这个两个变量选择最大值即可
        :param root:
        :return:
        """
        max_path = float('-inf')
        if root is None:
            return float('-inf')
        e_l = self.max_path_sum(root.left)
        e_r = self.max_path_sum(root.right)
        max_path = max(max_path, root.val + max(0, e_l) + max(0, e_r), e_l, e_r)
        return max_path

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先.
        :param root:
        :param p:
        :param q:
        :return:
        """
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

    def insert_into_bst(self, root: TreeNode, val: int):
        """
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点.
        :param root:
        :param val:
        :return:
        """

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
