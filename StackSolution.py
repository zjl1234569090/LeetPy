#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: StackSolution.py
@Created: 2020/9/21 4:11 下午
@Contact: jiulinzeng@tencent.com
@Description: 栈 相关的算法题解
"""
import math
from typing import List
import collections
from collections import deque


class Solution:
    @staticmethod
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        286. 墙与门
        https://leetcode-cn.com/problems/walls-and-gates/

        考察BFS
        :param self:
        :param rooms:
        :return:
        """

        def wallsAndGates(self, rooms: List[List[int]]) -> None:
            """
            Do not return anything, modify rooms in-place instead.
            """
            if not rooms:
                return rooms
            m, n = len(rooms), len(rooms[0])

            # Seach All Gatas
            room_queue = deque()
            for r in range(m):
                for c in range(n):
                    if rooms[r][c] == 0:
                        room_queue.append((r, c, 0))

            # Update Distance
            while room_queue:
                r, c, dist = room_queue.popleft()
                # Iterate in four directions
                for dr, dc in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
                    newr, newc = r + dr, c + dc
                    # Find [Valid & Unvisited & Empty] Room
                    if 0 <= newr < m and 0 <= newc < n and rooms[newr][newc] == 2147483647:
                        rooms[newr][newc] = dist + 1
                        room_queue.append((newr, newc, dist + 1))


    @staticmethod
    def longestPalindrome(s: str) -> str:
        """5. 最长回文子串
        https://leetcode-cn.com/problems/longest-palindromic-substring/
        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def decodeStringStack(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

    def decodeStringDFS(self, s: str) -> str:
        """
        394. 字符串解码(递归解法)
        https://leetcode-cn.com/problems/decode-string/
        :param s:
        :return:
        """

        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)

    def calculate(self, s: str) -> int:
        """
        227. 基本计算器 II
        https://leetcode-cn.com/problems/basic-calculator-ii/
        :param s:
        :return:
        """
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)

    def removeDuplicateLetters(self, s):
        """
        316. 去除重复字母
        https://leetcode-cn.com/problems/remove-duplicate-letters/
        :param s:
        :return:
        """
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

    def isValid(self, s: str) -> bool:
        """
        20. 有效的括号
        https://leetcode-cn.com/problems/valid-parentheses/
        :param s:
        :return:
        """
        if s == "":
            return True
        stack = []
        for ch in s:
            if len(stack) == 0 or ch in "{([":
                stack.append(ch)
            else:
                if ch == "}":
                    if stack[-1] == '{':
                        stack = stack[:-1]
                    else:
                        return False
                elif ch == ")":
                    if stack[-1] == '(':
                        stack = stack[:-1]
                    else:
                        return False
                elif ch == "]":
                    if stack[-1] == '[':
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

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
