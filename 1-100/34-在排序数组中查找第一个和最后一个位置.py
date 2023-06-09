# -*- encoding: utf-8 -*-
"""
@File    :   34-在排序数组中查找第一个和最后一个位置.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    elif target < nums[0] or target > nums[-1]:
        return [-1, -1]
    else:
        _l, r = 0, len(nums) - 1
        while _l <= r:
            mid = (_l + r) // 2
            if target > nums[mid]:
                _l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            elif target == nums[mid]:
                _l = r = mid
                while _l - 1 >= 0 and nums[_l - 1] == target:
                    _l -= 1
                while r + 1 <= len(nums) - 1 and nums[r + 1] == target:
                    r += 1
                return [_l, r]
    return [-1, -1]


nums = [1, 3, 4, 6, 8, 8, 9, 10]
a = searchRange(nums, 5)
print(a)
