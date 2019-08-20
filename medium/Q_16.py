#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 19:22
# @Author  : ck
"""
题目：<最接近的三数之和>
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。

    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 特判
        if len(nums) < 3:
            return []
        nums.sort()
        diff = -1
        for k in range(0, len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i, j = k + 1, len(nums) - 1

            while i < j:
                temp = nums[k] + nums[i] + nums[j]

                if diff < 0 or abs(temp - target) < diff:
                    diff = abs(temp - target)
                    result = temp

                if temp > target:
                    j -= 1
                elif temp < target:
                    i += 1
                else:
                    return target
        return result


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    result = s.threeSumClosest(nums, target)
    print(result)
