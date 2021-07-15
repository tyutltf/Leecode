# -*- encoding: utf-8 -*-
'''
@File    :   219-存在重复元素二.py
@Time    :   2021/07/15 19:14:42
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        # 自己写法 有问题
        # for i in range(len(nums)):
        #     if i-k >= 0:
        #         temp = nums[i-k:i+k+1]
        #     else:
        #         temp = nums[0:i+k+1]
        #     print(temp)
        #     if len(set(temp)) != len(temp):
        #         return True
        # else:
        #     return False

        hash = {}
        for i in range(len(nums)):
            if(nums[i] not in hash):
                hash[nums[i]] = i
            else:
                if(i-hash[nums[i]] <= k):
                    return True
                else:
                    hash[nums[i]] = i
        return False


obj = Solution()
nums = [1, 0, 1, 1]
k = 1
print(obj.containsNearbyDuplicate(nums, k))
