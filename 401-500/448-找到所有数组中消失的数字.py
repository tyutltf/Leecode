# -*- encoding: utf-8 -*-
'''
@File    :   448-找到所有数组中消失的数字.py
@Time    :   2021/07/01 23:27:05
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List


'''
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

 

示例 1：

输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
示例 2：

输入：nums = [1,1]
输出：[2]
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        all_nums = [i for i in range(1, len(nums)+1)]
        return list(set(all_nums)-set(nums))

        # counter = set(nums)
        # N = len(nums)
        # res = []
        # for i in range(1, N + 1):
        #     if i not in counter:
        #         res.append(i)
        # return res


obj = Solution()
print(obj.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
