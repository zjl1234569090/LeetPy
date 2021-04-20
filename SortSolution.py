#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: SortSolution.py
@Created: 2021/3/30 11:18 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from typing import List
import heapq


class Solution:

    def minNumber(self, nums: List[int]) -> str:
        """
        剑指 Offer 45. 把数组排成最小的数
        https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
        :param nums:
        :return:
        """
        s = [str(x) for x in nums]
        self.quick_sort4str(s, 0, len(s) - 1)
        return ''.join(s)

    @staticmethod
    def quick_sort4str(s: str, start: int, end: int):
        """

        :param s:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return
        i, j = start, end

        # 以最左边元素为参考元素
        while i < j:
            # 从右边一直找到比参考元素小的第一个元素
            while s[j] + s[start] >= s[start] + s[j] and i < j:
                j -= 1
            # 从左边找比参考元素大的最后一个元素
            while s[i] + s[start] <= s[start] + s[i] and i < j:
                i += 1
            if i < j:
                s[i], s[j] = s[j], s[i]
        s[i], s[start] = s[start], s[i]

        Solution.quick_sort4str(s, start, i - 1)
        Solution.quick_sort4str(s, i + 1, end)
        return s

    @staticmethod
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        """
        220. 存在重复元素 III
        https://leetcode-cn.com/problems/contains-duplicate-iii/
        :param nums:
        :param k:
        :param t:
        :return:
        """
        if t < 0 or k < 0:
            return False

        all_buckets = {}
        bucket_size = t + 1
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size
            if bucket_num in all_buckets:
                return True

            all_buckets[bucket_num] = nums[i]

            # 检查前一个桶
            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:
                return True

            # 检查后一个桶
            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:
                return True

            if i > k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False
