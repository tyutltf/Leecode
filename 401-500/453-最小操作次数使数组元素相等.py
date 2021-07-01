# -*- encoding: utf-8 -*-
'''
@File    :   453-最小操作次数使数组元素相等.py
@Time    :   2021/07/01 23:45:17
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。

 

示例：

输入：
[1,2,3]
输出：
3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

题意可理解位每次让一个值减去1，使得所有的值相等，那理想情况就是每个值最终等于最小值。

那么题目就转换为所有值减去最小值的和。
'''


class Solution:
    def minMoves(self, nums: List[int]):
        minvalue = min(nums)
        count = 0
        for i in nums:
            count += i - minvalue
        return count


obj = Solution()
print(obj.minMoves([1, 2, 3]))
