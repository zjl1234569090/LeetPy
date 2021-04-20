#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: jiulinzeng
@FileName: heapq_v2.py
@Created: 2021/4/18 8:09 下午
@Contact: jiulinzeng@tencent.com
@Description:
"""
from typing import List


def heapify(x):
    n = len(x)
    # 从第一个非叶子节点开始，自下而上调整
    for i in reversed(range(n // 2)):
        _siftup(x, i)


def heappush(heap, item):
    """

    :param heap:
    :param item:
    :return:
    """
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap: List):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def _siftup(heap, pos):
    """
    将pos后续的节点的孩子节点中较小者上浮
    :param heap:
    :param pos:
    :return:
    """
    endpos = len(heap)
    newitem = heap[pos]
    startpos = pos
    childpos = 2 * pos + 1
    while pos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and heap[rightpos] <= heap[childpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def _siftdown(heap, startpos, pos):
    """
    从 startpos 到 pos 向下调整堆
    :param heap:
    :param startpos:
    :param pos:
    :return:
    """
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        if heap[parentpos] > newitem:
            heap[pos] = heap[parentpos]
            pos = parentpos
            continue
        break
    heap[pos] = newitem
