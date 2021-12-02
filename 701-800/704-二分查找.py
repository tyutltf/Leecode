# -*- encoding: utf-8 -*-
'''
@File    :   704-二分查找.py
@Time    :   2021/12/01 21:13:43
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def search(self, nums: List[int], target: int):
        # * 普通的二分查找 数组为有序数组，同时题目还强调数组中无重复元素，因为一旦有重复元素，使用二分查找法返回的元素下标可能不是唯一的
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if target < nums[middle]:
                right = middle-1
            elif target > nums[middle]:
                left = middle+1
            else:
                return middle
        return -1


object = Solution()
nums, target = [-1, 0, 3, 5, 9, 12], 9
print(object.search(nums, target))
