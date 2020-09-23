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
