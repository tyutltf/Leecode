# -*- encoding: utf-8 -*-
"""
@File    :   88-合并两个有序数组.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # for x in nums2:
        #     i = m - 1
        #     while i > -1:
        #         if nums1[i] > x:
        #             nums1[i + 1] = nums1[i]
        #             i -= 1
        #         else:
        #             nums1[i + 1] = x
        #             break
        #     if i == -1:
        #         nums1[0] = x
        #     m += 1
        i = m - 1  # i=2
        j = n - 1  # j=2
        while j >= 0:
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]  # 把大的数放到nums1的最后一位，倒着放入
                i -= 1
            nums1[i + j + 1] = nums2[j]
            j -= 1

        return nums1


object = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6, 0]
n = 3
result = object.merge(nums1, m, nums2, n)
print(result)
