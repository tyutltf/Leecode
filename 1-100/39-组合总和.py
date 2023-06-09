# -*- encoding: utf-8 -*-
"""
@File    :   39-组合总和.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        length = len(candidates)
        if length == 0:
            return []
        if candidates[0] > target:
            return []
        re = []

        for i in range(length):
            num = candidates[i:]
            # print(num)
            temp = target - candidates[i]
            # print(temp)
            res = [candidates[i]]
            # print(res)
            if temp == 0:
                re.append(res)
            elif temp < 0:
                break
            else:
                a = self.combinationSum(num, temp)
                for k in a:
                    k = res + k
                    re.append(k)
        return re


object = Solution()
candidates = [2, 3, 5, 8]
target = 8
print(object.combinationSum(candidates, target))
