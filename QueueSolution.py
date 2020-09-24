#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: QueueSolution.py
@Created: 2020/9/23 4:12 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from typing import List
from collections import deque


class Solution:
    def update_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。 两个相邻元素间的距离为 1
        思路 1: 从 0 开始 BFS, 遇到距离最小值需要更新的则更新后重新入队更新后续结点
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        row_num, col_num = len(matrix), len(matrix[0])
        dist_mat = [[float('inf')] * col_num for _ in range(row_num)]

        bfs = deque([])
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == 0:
                    dist_mat[i][j] = 0
                    bfs.append((i, j))

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(bfs) > 0:
            i, j = bfs.popleft()
            for neighbor_i, neighbor_j in neighbors:
                n_i, n_j = i + neighbor_i, j + neighbor_j
                if 0 <= n_i < row_num and 0 <= n_j < col_num:
                    if dist_mat[n_i][n_j] > dist_mat[i][j] + 1:
                        dist_mat[n_i][n_j] = dist_mat[i][j] + 1
                        bfs.append((n_i, n_j))
        return dist_mat

        # ----------------------------------------------------------------------
        # 单调栈的拓展，可以从数组头 pop 出旧元素，典型应用是以线性时间获得区间最大/最小值。|
        # ----------------------------------------------------------------------

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        """
        给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
        滑动窗口每次只向右移动一位。 返回滑动窗口中的最大值。  
        进阶：
        你能在线性时间复杂度内解决此题吗？

        :param nums:
        :param k:
        :return:
        """
        nums_len = len(nums)
        if nums_len * k == 0:
            return []
        if k == 1:
            return nums
        max_queue = deque()
        result = []
        for i in range(nums_len):

            # 维护一个长度为k 的单调递增队列, 即队头元素最大, 队尾元素最小
            if max_queue and max_queue[0] == i - k:
                max_queue.popleft()  # 长度超过k 最pop 出对头元素
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()  # 新来的元素大于队尾元素，需要调整
            max_queue.append(i)  # 每个元素都要进入队列进行处理

            if i >= k - 1:  # 保证窗口长度至少为 k 后, 才开始输出结果
                result.append(nums[max_queue[0]])  # 队列的头元素最大
        return result

    def shortest_subarray(self, A: List[int], K: int) -> int:
        """
        返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
        如果没有和至少为 K 的非空子数组，返回 -1 。
        :param A:
        :param K:
        :return:
        """
        N = len(A)
        cdf = [0]  # 数组A的累积和数组
        for num in A:
            cdf.append(cdf[-1] + num)

        result = N + 1
        min_queue = deque()

        for i, csum in enumerate(cdf):

            # 维护一个单调减 队列
            while min_queue and csum <= cdf[min_queue[-1]]:
                # 如果当前位置的元素 比 队尾的元素还小，需要调整队尾元素
                min_queue.pop()

            # 在单调减队列 基础上 检索满足条件的最短子数组的长度
            while min_queue and csum - cdf[min_queue[0]] >= K:
                result = min(result, i - min_queue.popleft())

            min_queue.append(i)

        return result if result <= N else -1


if __name__ == '__main__':
    qs = Solution()
    print(qs.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
