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
from typing import List


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
                self.result.append(root.val)  # 先遍历根节点
                stack.append(root)  # 关键点! 存储已经遍历的节点, 用于后续回溯右节点
                root = root.left  # 再遍历左节点

            # 回溯右节点
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
            while root is not None:  # 任何一棵子树, 先遍历至最左边的子节点
                stack.append(root)
                root = root.left

            node = stack.pop()  # 左/中
            self.result.append(node.val)  # 左/中
            root = node.right  # 右
        return self.result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []  # 用来存储后序遍历节点的值
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                # 判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            # 循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop()  # 取出栈顶元素进行访问
            res.append(node.val)  # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node:  # 若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right  # 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res

    @staticmethod
    def post_order_traversal(root: TreeNode):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]

    def level_order(self, root: TreeNode):
        """
        层次遍历
        :param root:
        :return:
        """
        if root is None:
            return self.result
        bfs = collections.deque([root])
        while len(bfs) > 0:  # 逐层遍历
            self.result.append([])
            level_size = len(bfs)
            for _ in range(level_size):  # 遍历层中的每一个节点
                node = bfs.popleft()
                self.result[-1].append(node.val)

                # 将子节点入队列, 用于后续遍历
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

    @staticmethod
    def insert_into_bst(root: TreeNode, val: int):
        """
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点.
        :param root:
        :param val:
        :return:
        """

        if root is None:  # 临界点 不要漏
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

    @staticmethod
    def zigzag_level_order(root: TreeNode):

        levels = []  # 遍历结果
        if root is None:
            return levels

        s = collections.deque([root])

        start_from_left = True
        while len(s) > 0:
            levels.append([])
            level_size = len(s)

            if start_from_left:
                for _ in range(level_size):
                    node = s.popleft()  # popleft
                    levels[-1].append(node.val)
                    if node.left is not None:
                        s.append(node.left)  # append
                    if node.right is not None:
                        s.append(node.right)  # append
            else:
                for _ in range(level_size):
                    node = s.pop()  # pop
                    levels[-1].append(node.val)
                    if node.right is not None:
                        s.appendleft(node.right)  # appendleft
                    if node.left is not None:
                        s.appendleft(node.left)  # appendleft

            start_from_left = not start_from_left

        return levels
