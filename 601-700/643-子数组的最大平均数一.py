# -*- encoding: utf-8 -*-
'''
@File    :   643-子数组的最大平均数一.py
@Time    :   2021/08/11 22:08:23
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int):
        # # 暴力法则 超时
        # res = -10000
        # for i in range(len(nums)-(k-1)):
        #     temp = nums[i:i+k]
        #     avg = sum(temp)/k
        #     print(avg)
        #     if res < avg:
        #         res = avg
        # return res

        i = 0
        print(nums[:k])
        total = sum(nums[:k])
        print(total)
        tmp = sum(nums[:k])
        print(tmp)
        for num in nums[k:]:
            tmp = tmp - nums[i] + num
            total = max(total, tmp)
            i += 1
        return total / k


obj = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(obj.findMaxAverage(nums, k))
