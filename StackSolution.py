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
    def eval_rpn(self, tokens:List[str]):
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

