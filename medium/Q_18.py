#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 16:56
# @Author  : ck
"""
题目：<四数之和>
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
    使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    注意：答案中不可以包含重复的四元组。

    示例：给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

            满足要求的四元组集合为：
            [
              [-1,  0, 0, 1],
              [-2, -1, 1, 2],
              [-2,  0, 0, 2]
            ]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):  # 固定两个数
                left = j + 1  # 左指针
                right = len(nums) - 1  # 右指针
                while right > left:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    if temp > target: right -= 1  # 太大了，右指针左移
                    if temp < target: left += 1  # 反之
        # 去重
        rec = []
        for i in ans:
            rec.append(list(i))
        return rec


if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    rec = s.fourSum(nums, target)
    print(rec)
