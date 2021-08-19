# -*- encoding: utf-8 -*-
'''
@File    :   674-最长连续递增序列.py
@Time    :   2021/08/18 19:47:29
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''

给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1：

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
示例 2：

输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。
'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]):
        # 常规解法 循环
        # length = len(nums)
        # maxres = 1
        # cache = 1
        # for i in range(length-1):
        #     if nums[i] < nums[i+1]:
        #         cache += 1
        #         maxres = max(maxres, cache)
        #     else:
        #         cache = 1
        # return maxres

        # 滑动窗口法  看题解
        if not nums:
            return 0
        le = ri = 0
        max_len = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ri = i
            else:
                if ri - le + 1 > max_len:
                    max_len = ri - le + 1
                le = ri = i
        return max(max_len, ri - le + 1)


obj = Solution()
nums = [1, 3, 5, 4, 7]
print(obj.findLengthOfLCIS(nums))
