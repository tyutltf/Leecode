# -*- encoding: utf-8 -*-
'''
@File    :   413-等差数列划分.py
@Time    :   2021/08/10 21:47:12
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]):
        res = 0
        if len(nums) < 3:
            return res
        # 差值数组
        coins = []
        for i in range(len(nums)-1):
            coins.append(nums[i+1]-nums[i])
        print(coins)
        # 差值个数数组
        cons = []
        a = 1
        for i in range(1, len(coins)):
            if coins[i] == coins[i - 1]:
                a += 1
            else:
                cons.append(a)
                a = 1
        cons.append(a)
        print(cons)
        # 计算最终个数 因为是差值 所以得加一
        cons = [i+1 for i in cons]
        print(cons)
        # 计算公式为 n-1 * n-2 最后除以 2
        for i in cons:
            temp = (i-2)*(i-1)/2
            res += temp
        return int(res)


nums = [1, 2, 3, 4, 5, 6, 12, 14, 16]
obj = Solution()
print(obj.numberOfArithmeticSlices(nums))
