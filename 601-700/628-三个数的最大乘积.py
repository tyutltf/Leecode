# -*- encoding: utf-8 -*-
'''
@File    :   628-三个数的最大乘积.py
@Time    :   2021/08/11 23:44:31
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maximumProduct(self, nums: List[int]):
        nums.sort()
        print(nums)
        # 全正数 或者 全负数
        res1 = nums[-1]*nums[-2]*nums[-3]
        # 有正数有负数
        res2 = nums[0]*nums[1]*nums[-1]
        return max(res1, res2)


obj = Solution()
nums = [-1, -2, -3, -4]
print(obj.maximumProduct(nums))
