#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: PriorityQueue.py
@Created: 2020/9/27 10:21 上午
@Contact: jiulinzeng@tencent.com
@Description: 优先级队列 (堆 heap)，Heap 可以高效地取出或更新当前池中优先级最高的元素，因此适用于一些需要 greedy 算法的场景。
"""
from typing import List
import heapq


class KthLargest:
    """
    设计一个找到数据流中第K大元素的类。
    遍历数据时，使用一个最小堆来维护当前最大的 K 个数据，堆顶数据为这 K 个数据中最小，即是你想要的第 k 个最大数据。
    每检查一个新数据，判断是否大于堆顶，若大于，说明堆顶数据小于了 K 个值，不是我们想找的第 K 个最大，
    则将新数据 push 进堆并 pop 掉堆顶，若小于则不操作，这样当遍历完全部数据后堆顶即为想要的结果。找最小时换成最大堆即可。

    这里用到的 heapq 库 参考：https://docs.python.org/zh-cn/3/library/heapq.html
    """

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.min_heap = []
        for num in nums:
            if len(self.min_heap) < self.K:
                heapq.heappush(self.min_heap, num)
            elif num > self.min_heap[0]:
                # 将 item 放入堆中，然后弹出并返回 heap 的最小元素。
                # 该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
                heapq.heappushpop(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.K:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)

        return self.min_heap[0]


class Solution:
    def k_smallest_pairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/
        给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
        定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
        找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

        :param nums1:
        :param nums2:
        :param k:
        :return:
        """

        m, n = len(nums1), len(nums2)
        result = []

        if m * n == 0:
            return result

        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set()

        while min_heap and len(result) < k:
            _, i1, i2 = heapq.heappop(min_heap)
            result.append([nums1[i1], nums2[i2]])
            if i1 < m - 1 and (i1 + 1, i2) not in seen:
                heapq.heappush(min_heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                seen.add((i1 + 1, i2))
            if i2 < n - 1 and (i1, i2 + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                seen.add((i1, i2 + 1))

        return result
