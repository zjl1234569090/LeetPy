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
from random import randint
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

    def merge_sort_v0(self, arr):
        """归并排序"""
        if len(arr) == 1:
            return arr
        # 使用二分法将数列分两个
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # 使用递归运算
        return self.merge_v0(self.merge_sort_v0(left), self.merge_sort_v0(right))

    def merge_v0(self, left, right):
        """排序合并两个数列"""
        result = []
        # 两个数列都有值
        while len(left) > 0 and len(right) > 0:
            # 左右两个数列第一个最小放前面
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 只有一个数列中还有值，直接添加
        result += left
        result += right
        return result

    def merge_sort_v1(self, nums: List[int]):
        """
        非递归
        """
        n = len(nums)
        if n <= 1:
            return nums
        sorted_size = 1  # 当前有序子数组的长度, 初始化 1
        while sorted_size < n:
            left = 0
            while left < n:
                m = left + sorted_size - 1
                if m >= n:
                    break
                right = min(m + sorted_size, n - 1)
                # print("left:", nums[left:m + 1], "right:", nums[m + 1:right + 1])
                nums[left:right + 1] = self.merge_v0(nums[left:m + 1], nums[m + 1:right + 1])
                # print(nums)
                left = right + 1
            sorted_size <<= 1
        return nums

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


if __name__ == '__main__':
    solution = Solution()

    test_num = 10000
    succ = 0
    fail = 0
    for _ in range(test_num):
        nums_len = randint(1, 1000)
        nums = [randint(0, 10) for _ in range(nums_len)]
        print("Before sorting:", nums)
        ans = sorted(nums)
        ans0 = solution.merge_sort_v1(nums)
        ok = all(x[0] == x[1] for x in zip(ans, ans0))
        if ok:
            succ += 1
            print("After sorting:", ans0)
            print("Nice")
        else:
            print(ans)
            print(ans0)
            print("Failed !")
            break
    print("test_num:{}, succ:{}".format(test_num, succ))
