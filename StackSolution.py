#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: StackSolution.py
@Created: 2020/9/21 4:11 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from typing import List


class Solution:
    def eval_rpn(self, tokens: List[str]):
        """
        波兰表达式计算 > 输入: ["2", "1", "+", "3", "*"] > 输出: 9 解释: ((2 + 1) * 3) = 9
        思路：通过栈保存原来的元素，遇到表达式弹出运算，再推入结果，重复这个过程
        :param tokens:
        :return:
        """

        def compute(or1, op, or2):
            """

            :param or1:
            :param op:
            :param or2:
            :return:
            """
            if op == "+":
                return or1 + or2
            elif op == "-":
                return or1 - or2
            elif op == "*":
                return or1 * or2
            elif op == "/":
                abs_result = abs(or1) // abs(or2)
                return abs_result if or1 * or2 > 0 else -abs_result

        stack = []
        for token in tokens:
            if token in ["+", "-", "*", '/']:
                or2 = stack.pop()
                or1 = stack.pop()
                stack.append(compute(or1, token, or2))
            else:
                stack.append(int(token))
        return stack[0]

    def decode_string(self, s: str):
        """
        给定一个经过编码的字符串，返回它解码后的字符串。 s = "3[a]2[bc]", 返回 "aaabcbc".
        s = "3[a2[c]]", 返回 "accaccacc". s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
        思路：通过两个栈进行操作，一个用于存数，另一个用来存字符串
        :param s:
        :return:
        """
        stack_str = ['']
        stack_num = []
        num = 0
        for c in s:
            if '0' <= c <= '9':
                num = 10 * num + int(c)
            elif c == '[':
                stack_num.append(num)
                stack_str.append('')
                num = 0
            elif c == ']':
                cur_str = stack_str.pop()
                stack_str[-1] += cur_str * stack_num.pop()
            else:
                stack_str[-1] += c
        return stack_str[0]

    def number_islands(self, grid: List[List[str]]):
        """

        :param grid:
        :return:
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and self.dfs_4_number_islands(grid, i, j) >= 1:
                    count += 1
        return count

    def dfs_4_number_islands(self, grid: List[List[str]], i: int, j: int):
        """

        :param grid:
        :param i:
        :param j:
        :return:
        """
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == '1':
            # 标记已经访问过的元素
            grid[i][j] = 0
            return self.dfs_4_number_islands(grid, i - 1, j) + self.dfs_4_number_islands(
                grid, i, j - 1) + self.dfs_4_number_islands(
                grid, i + 1, j) + self.dfs_4_number_islands(grid, i, j + 1) + 1
        return 0

    # --------------------------------------------------------------------------------------
    # 单调栈即是栈中元素有单调性的栈，典型应用为用线性的时间复杂度找左右两侧第一个大于/小于当前元素的位置。|
    # --------------------------------------------------------------------------------------
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """
        思路：包含当前 bar 最大矩形的边界为左边第一个高度小于当前高度的 bar 和右边第一个高度小于当前高度的 bar
        关键点: 单调栈
        :param heights:
        :return:
        """

        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack) - 1):
            max_res = max(max_res, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
        return max_res

    def trap(self, height: List[int]):
        """
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        https://leetcode-cn.com/problems/trapping-rain-water/
        关键点: 单调栈
        :param height:
        :return:
        """
        stack = []
        result = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                if not stack:
                    break
                result += (min(height[stack[-1]], height[i]) - height[cur]) * (i - stack[-1] - 1)
            stack.append(i)
        return result
