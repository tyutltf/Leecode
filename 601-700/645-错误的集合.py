# -*- encoding: utf-8 -*-
'''
@File    :   645-错误的集合.py
@Time    :   2021/08/12 20:54:21
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findErrorNums(self, nums: List[int]):
        # 错误解法
        # lenth = len(nums)
        # real_list = [i for i in range(1, lenth+1)]
        # print(real_list)
        # for i in range(lenth):
        #     if nums[i] != real_list[i]:
        #         res = [nums[i], real_list[i]]
        # return res

        # 这道题做不出来的，肯定是上学的时候数学老师长得不够漂亮！

        # 纯数学的角度解题：
        # sum(nums) - sum(set(nums)) = 重复的数字
        # (1 + len(nums)) * len(nums) // 2 - sum(set(nums)) = 丢失的数字

        # 循环数组
        # 如何一次for循环获取到重复的数字和丢失的数字呢？

        # 我们需要对数组进行排序
        # 重复的数字就是nums[i + 1] == nums[i]
        # 丢失的数字呢需要分情况考虑
        # 当nums[0] ！= 1，丢失的数字是1
        # 当nums[-1] != len(nums),丢失的数字是len(nums)
        # 排除上面两种场景，那么当nums[i + 1] - nums[i] = 2时，
        # 丢失的数字为nums[i] + 1
        # 哈希表操作

        # 使用Counter将nums转化为一个字典dict
        # 然后for循环1 -- n
        # 没有在dict中找到的数字为丢失的
        # 找到的数字value为2的便是重复的

        ln, total = len(nums), sum(set(nums))
        return [sum(nums) - total, (1 + ln) * ln // 2 - total]


obj = Solution()
nums = [1, 2, 2, 4]
print(obj.findErrorNums(nums))
