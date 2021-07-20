# -*- encoding: utf-8 -*-
'''
@File    :   496-下一个更大元素1.py
@Time    :   2021/07/20 21:44:13
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        # nums3 = sorted(nums2)
        # print(nums3)
        # res_list = []
        # for i in range(len(nums1)):
        #     temp = nums3.index(nums1[i])
        #     print(temp)
        #     if temp != len(nums2)-1:
        #         new_nums2 = nums2[i::]
        #         print(new_nums2)
        #         res = new_nums2.index(temp+1)
        #     else:
        #         res = -1
        #     res_list.append(res)
        # return res_list

        # 字典存储结果
        total_list = {}
        # 遍历每个元素
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                # 第一个比当前值大的元素即是当前值key的value
                if nums2[j] > nums2[i]:
                    total_list[nums2[i]] = nums2[j]
                    break
                # 如果没有则-1
                if j == len(nums2) - 1:
                    total_list[nums2[i]] = -1
        total_list[nums2[-1]] = -1
        result = []
        # 返回每个key值对应的value
        for num in nums1:
            result.append(total_list[num])
        return result


obj = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(obj.nextGreaterElement(nums1, nums2))
