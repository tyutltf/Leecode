# -*- encoding: utf-8 -*-
"""
@File    :   53-最大子序和.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0

        return max_sub_sum


object = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = object.maxSubArray(nums)
print(result)
