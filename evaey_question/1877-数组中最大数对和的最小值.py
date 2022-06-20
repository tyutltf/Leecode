# -*- encoding: utf-8 -*-
'''
@File    :   1877-数组中最大数对和的最小值.py
@Time    :   2021/07/20 20:24:43
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。

比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：

nums 中每个元素 恰好 在 一个 数对中，且
最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。

示例 1：

输入：nums = [3,5,2,3]
输出：7
解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
示例 2：

输入：nums = [3,5,4,2,4,6]
输出：8
解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minPairSum(self, nums: List[int]):
        # 思路 数组排序 然后首尾配 求出最大的
        nums.sort()
        n = len(nums)
        ans = 0
        num_pairs = n // 2
        for i in range(num_pairs):
            if ans < nums[i] + nums[n - 1 - i]:
                ans = nums[i] + nums[n - 1 - i]
            print(ans)
        return ans


obj = Solution()
nums = [1, 5, 2, 3, 4, 4]
print(obj.minPairSum(nums))
