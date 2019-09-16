#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 11:22
# @Author  : ck
"""
题目:<搜索旋转排序数组>
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。

    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

    你可以假设数组中不存在重复的元素。

    你的算法时间复杂度必须是 O(log n) 级别。

    示例 1:

    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
    示例 2:

    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1
"""

import bisect
from typing import List


class Solution:
    def search(self, nums: List, target: int) -> int:
        """
        二分法找到断点的位置恢复原始数组，然后正常二分法即可
        python 中 bisect 模块针对的是 list, 如果直接构造 list，
        相当于遍历所有元素，时间复杂度为 O(N) 而不是 O(logN)，
        因此我们修改当前类的魔法方法伪造 list，然后用当前类代替list

        :param nums: 旋转后数组
        :param target: 待搜索目标值
        :return: 下标
        """
        lo, hi, k = 0, len(nums) - 1, -1
        while lo <= hi:
            m = (lo + hi) // 2
            if m == len(nums) - 1 or nums[m] > nums[m + 1]:
                k = m + 1
                break
            elif m == 0 or nums[m] < nums[m - 1]:
                k = m
                break
            if nums[m] > nums[0]:
                lo = m + 1
            else:
                hi = m - 1
        i = (bisect.bisect_left(nums[k:] + nums[:k], target) + k) % max(len(nums), 1)
        return i if nums and nums[i] == target else -1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    print(s.search(nums, target))
