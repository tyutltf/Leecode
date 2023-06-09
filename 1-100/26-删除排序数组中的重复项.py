# -*- encoding: utf-8 -*-
"""
@File    :   26-删除排序数组中的重复项.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
"""


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
i = 0
while i < len(nums):
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        nums.pop(i + 1)
    i += 1
print(nums)
