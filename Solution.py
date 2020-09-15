#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: Solution.py
@Created: 2020/9/15 9:52 上午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from StructCollections import *


class Solution:

    def __init__(self):
        pass

    def merge_sort(self, nums):
        """
        归并排序
        :param list nums: 待排序数组
        :return: 排序后的数组
        """
        if len(nums) < 1:
            return nums
        mid = len(nums) / 2
        left_nums = self.merge_sort(nums[:mid])
        right_nums = self.merge_sort(nums[mid:])
        return self._merge(left_nums, right_nums)

    def _merge(self, left_nums, right_nums):
        """
        数组有序归并
        :param list left_nums:
        :param list right_nums:
        :return: 归并后的数组
        """
        result = []
        l, r = 0, 0
        while l < len(left_nums) and r < len(right_nums):
            if left_nums[l] > right_nums[r]:
                result.append(right_nums[r])
                r += 1
            else:
                result.append(left_nums[l])
                r += 1
        result += left_nums[l:]
        result += right_nums[r:]
        return result

    def quick_sort(self, nums, start, end):
        """
        快速排序.
        :param list nums: 待排序数组
        :param int start: 起始
        :param int end: 终止
        :return: 已排序数组
        """
        if len(nums) <= 1:
            return nums
        if start < end:  # 此处判断容易被遗漏,多加关注
            pivot = self._partition(nums, start, end)
            self.quick_sort(nums, 0, pivot - 1)
            self.quick_sort(nums, pivot + 1, end)
        return nums

    def _partition(self, nums, start, end):
        """
        将数组划分为左右两段, 左边段小于右边段
        :param list nums: 待划分数组
        :param int start: 起始
        :param int end: 终止
        :return: 分界点
        """

        p = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < p:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i


if __name__ == '__main__':
    nums_1 = [1, 3, 2, 8, 6, 4, 5, 10, 9, 0, 7]
    solution = Solution()
    solution.quick_sort(nums_1, 0, len(nums_1) - 1)
    print(nums_1)
