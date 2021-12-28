# -*- encoding: utf-8 -*-
'''
@File    :   747-至少是其他数字两倍的最大数.py
@Time    :   2021/12/28 20:02:06
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。

请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

示例 1：

输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 大于数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。
其他元素 第二大
示例 2：

输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。
示例 3：

输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # 求出最大和二大 看最大是否超出二大的二倍
        if len(nums) == 1:
            return 0
        # max_num, max_index, less = 0, 0, 0
        # for i in range(len(nums)):
        #     if nums[i] > max_num:
        #         less = max_num
        #         max_num = nums[i]
        #         max_index = i
        #     elif nums[i] > less:
        #         less = nums[i]
        # # print(max_num, less, max_index)
        # if max_num >= less*2:
        #     return max_index
        # else:
        #     return -1

        sortnums = sorted(nums)
        if sortnums[-1] >= sortnums[-2]*2:
            return nums.index(sortnums[-1])
        else:
            return -1


obj = Solution()
nums = [3, 6, 1, 0]
print(obj.dominantIndex(nums))
