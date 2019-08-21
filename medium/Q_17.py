#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 18:55
# @Author  : ck
"""
题目：<电话号码的字母组合>
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    示例:
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    说明:
    尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
# a = ["a", "b", "c"]
# b = ["q", "w", "e"]
# m = [x + y for x in a for y in b]
# print(m)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits: return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1


if __name__ == "__main__":
    s = Solution()
    digits = "23"
    result = s.letterCombinations(digits)
    print(result)
